import discord
from discord import app_commands
from discord.ext import commands

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @app_commands.command(name="status", description="Check connection status of server.")
        async def status(self, interaction: discord.Interaction):
            await interaction.response.defer()

            statuses = self.bot.connections.get_all_statuses()

            embed = discord.Embed(
                title="System Status",
                description="Current connection status for external services.",
                color=discord.Color.blue()
            )

            for service, status in statuses.items():
                embed.add_field(name=service, value=status, inline=False)

            await interaction.followup.send(embed=embed)

        async def setup(bot):
            await bot.add_cog(Status(bot))
