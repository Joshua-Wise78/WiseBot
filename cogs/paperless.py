import discord
import httpx
import os
import io
import uuid
from datetime import datetime
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv


load_dotenv()
try:
    LOCAL_IP = os.environ["LOCAL_IP"]
    TAILSCALE_IP = os.environ["TAILSCALE_IP"]
except KeyError as e:
    print(f"Missing enviornment variable {e}")

class Paperless(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = None
    
    @app_commands.command(name="upload-document", description="Upload photo to paperless-ngx")
    async def upload_document(self, interaction: discord.Interaction, document: discord.Attachment):
        pass

    @app_commands.command(name="retrieve-document", description="Retrieve document from paperless-ngx")
    async def retrieve_document(self, interaction: discord.Interaction):
        pass
