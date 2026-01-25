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
from immich_client.api.memories import search_memories
from immich_client.models import AssetMediaCreateDto
from immich_client.types import File
from immich_client.api.server import get_server_version 

from immichUtils import ( check_immich_connection,
     convert_search_response_dto,
     upload_image,
     list_memories,
     get_asset_thumbnail
 )

"""
 TODO:
     1. Refactor code move server connection into its own cog and connection points.
     2. Add a random photo grabber function.
     3. Refactor output for getMemories function to not spam the server.
     4. Add support for videos.
     5. Add function to favorite images and filter them?
     6. Album smart sort? (This one will suck)
     
 """

load_dotenv()
try:
    IMMICH_KEY = os.environ["IMMICH_KEY"]
    LOCAL_IP = os.environ["LOCAL_IP"]
    TAILSCALE_IP = os.environ["TAILSCALE_IP"]
except KeyError as e:
    print(f"Missing enviornment variable {e}")

class Immich(commands.Cog):
    """
        ADD:
            1. send-photo toggle for if the photo is favorite or not
    """
    def __init__(self, bot):
        self.bot = bot
        self.client = None

    async def cog_load(self):
        """
          Initalizes the Immich client by connecting to the Local_IP first then
          falling back on Tailscale as a secondary connection.  
        """
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
        """
          Attempts to use httpx to ping the client to check for a connection  
        """
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
        """
            Slash command used to call check_immich_connection to see if the
            client is connected to Immich's api or not.  
        """
        response  = check_immich_connection(self)            
        await interaction.response.send_message(response)

    @app_commands.command(name="send-photo", description="Send a photo to Immich instance.")
    async def sendImg(self, interaction: discord.Interaction, photo: discord.Attachment):
        """
          Slash command that sends a photo to immich calling upload_image from
          immichUtils  
        """
        await interaction.response.defer(thinking=True)
        try:
            response = await upload_image(self, photo)
            await interaction.followup.send(f"{response}")
        except Exception as e:
             await interaction.followup.send(f"Error uploading file: {str(e)}")

    # Search for an image using smart_search feature from Immich
    @app_commands.command(name="search-photo", description="Smart search image with query.")
    async def searchImg(self, interaction: discord.Interaction):
        await interaction.response.send_message("Not implemented currently.")

    @app_commands.command(name="memories", description="List up to 5 memories from date {XXXX-XX-XX}")
    async def getMempory(self, interaction: discord.Interaction, date: str):
        await interaction.response.defer(thinking=True)

        try:
            search_res, error = await list_memories(self, date)                

            if error:
                await interaction.followup.send(error)
                return

            asset_list, error = await convert_search_response_dto(search_res)

            if error:
                await interaction.followup.send(error)
                return

            if not asset_list:
                await interaction.followup.send(f"No memories found for {date}.")
                return

            count = 0
            for asset in asset_list[:5]:
                
                try:
                    image_bytes, img_error = await get_asset_thumbnail(self, asset.id)

                    if img_error:
                        await interaction.followup.send(f"Could not load image for {asset.original_file_name}: {img_error}")
                        continue

                    file = discord.File(io.BytesIO(image_bytes), filename=asset.original_file_name)

                    embed = discord.Embed(
                        title=f"Memory: {asset.original_file_name}",
                        description=f"Created: {asset.file_created_at.strftime('%Y-%m-%d %H:%M:%S')}",
                        color=discord.Color.blue()
                    )
                    embed.set_image(url=f"attachment://{asset.original_file_name}")

                    await interaction.followup.send(embed=embed, file=file)
                    count += 1
                except Exception as loop_error:
                    print(f"Error processing asset {asset.id}: {loop_error}")
                    continue
            
            if count == 0:
                await interaction.followup.send("Found assets, but failed to download any images.")

        except Exception as e:
            await interaction.followup.send(f"Error listing memories: {str(e)}")

async def setup(bot):
    await bot.add_cog(Immich(bot))
