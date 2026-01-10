import discord
from discord.ext import commands
from discord import app_commands

class Server(commands.Cog):
    """
        TODO:
            1. API setup for Immich
            2. API setup for Crafty
            3. API setup for Docker updates
    """
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="test", description="Testing command")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello!")

async def setup(bot):
    await bot.add_cog(Server(bot))
