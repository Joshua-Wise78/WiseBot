import discord
import httpx
import os
import io
import uuid
from datetime import datetime
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

from ..server.paperless.paperless_utils import (
    upload_document
)


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

    async def cog_load(self):
        """
          Initalizes the Paperless client by connecting to the Local_IP first then
          falling back on Tailscale as a secondary connection.  
        """
        self.client = self.bot.connections.paperless_client

        if self.client:
            print("Paperless cog successfully loaded.")
        else:
            print("Paperless cog loaded, but Paperless client is currently not connected")

    
    @app_commands.command(name="upload-document", description="Upload photo to paperless-ngx")
    async def upload_document(self, interaction: discord.Interaction, document: discord.Attachment):
        """
          Paperless uses the pathway
              /api/documents/post_document/

          The API client generated used two files.
          1. documents_post_document_create.py - This is the API call that we will use to build a file
          2. post_document_request.py - This is the model of the file to be uploaded aka the body
        """
        await interaction.response.defer(thinking=True)
        try:
            response = await upload_document(self, document)
            await interaction.followup.send(f"{response}")
        except Exception as e:
            await interaction.followup.send(f"Error uploaded document: {str(e)}")

    @app_commands.command(name="retrieve-document", description="Retrieve document from paperless-ngx")
    async def retrieve_document(self, interaction: discord.Interaction):
        pass

async def setup(bot):
    await bot.add_cog(Paperless(bot))
