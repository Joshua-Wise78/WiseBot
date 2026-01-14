import discord
import httpx
import os
import io
import uuid
from datetime import datetime
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

from immich_client import AuthenticatedClient 
from immich_client.api.assets import upload_asset
from immich_client.models import AssetMediaCreateDto
from immich_client.types import File
from immich_client.api.server import get_server_version 

load_dotenv()
try:
    IMMICH_KEY = os.environ["IMMICH_KEY"]
    LOCAL_IP = os.environ["LOCAL_IP"]
    TAILSCALE_IP = os.environ["TAILSCALE_IP"]
except KeyError as e:
    print(f"Missing enviornment variable {e}")

class Immich(commands.Cog):
    """
        TODO:
            1. API setup for Immich
            2. Search images
            3. Server status
    """
    def __init__(self, bot):
        self.bot = bot
        self.client = None

    async def cog_load(self):
        local_url = f"http://{LOCAL_IP}:2283"
        local_attempt = await self.check_connection(local_url)

        if local_attempt:
            self.client = AuthenticatedClient(base_url=local_url + "/api",
                                             token=IMMICH_KEY)
            print("Connected through Local Address.")

        if not local_attempt:
            print("Local Address did not find Immich.")
            tailscale_url = f"http://{TAILSCALE_IP}:2283"
            vpn_attempt = await self.check_connection(tailscale_url)

            if vpn_attempt:
                self.client = AuthenticatedClient(base_url=tailscale_url + "/api",
                                                   token=IMMICH_KEY,
                                                   auth_header_name="x-api-key",
                                                   prefix="")
                print("Connected through Tailscale.")

    async def check_connection(self, url):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{url}/server-info/ping",
                                             timeout=2.0)
                if response.status_code == 200:
                    return url
        except Exception:
            return None
        return None

    @app_commands.command(name="check-immich-connection",
                          description="Check Immich status.")
    async def status(self, interaction: discord.Interaction):
        if not self.client:
            await interaction.response.send_message(f"Error: Not connected")
        else:
            await interaction.response.send_message(f"Connected to {self.client._base_url}")

    @app_commands.command(name="send-photo", description="Send a photo to Immich instance.")
    async def sendImg(self, interaction: discord.Interaction, photo: discord.Attachment):
        await interaction.response.defer(thinking=True)

        try:
            file_bytes = await photo.read()
            file_stream = io.BytesIO(file_bytes)

            device_asset_id = f"discord-{photo.id}-{uuid.uuid4()}"

            immich_file = File(
                payload=file_stream,
                file_name=photo.filename,
                mime_type=photo.content_type or "image/jpeg"
            )

            body = AssetMediaCreateDto(
                asset_data=immich_file,
                device_asset_id=device_asset_id,
                device_id="discord-bot",
                file_created_at=datetime.now(),
                file_modified_at=datetime.now(),
            )

            if self.client is None:
                await interaction.followup.send(f"Upload not possible not connected to immich client")
            else:
                response = upload_asset.sync(
                    client=self.client,
                    body=body
                )

                if response:
                    await interaction.followup.send(f"Successfully uploaded: `{photo.filename}` to immich")
                else:
                    await interaction.followup.send(f"Upload failed. No response from immich.")
            

        except Exception as e:
            await interaction.followup.send(f"Error uploading file: {str(e)}")

async def setup(bot):
    await bot.add_cog(Immich(bot))
