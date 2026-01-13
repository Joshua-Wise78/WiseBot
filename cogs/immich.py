import discord
import httpx
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

from immich_client import AuthenticatedClient 
from immich_client.api.authentication import login
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
                                                   token=IMMICH_KEY)
                print(tailscale_url)
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

    @commands.command()
    async def status(self, ctx):
        if not self.client:
            await ctx.send("Bot is not connected to Immich.")
            return
        await ctx.send(f"Currently connected to: {self.client._base_url}")

async def setup(bot):
    await bot.add_cog(Immich(bot))
