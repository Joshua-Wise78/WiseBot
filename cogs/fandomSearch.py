import discord
from discord.ext import commands
from discord import app_commands

from jsonUtils import save_to_json, retrieve_from_json, list_sites, search_sites
from server.fandom.fandom import get_fandom, retrieve_from_json

class FandomSearch(commands.Cog):
    """
    TODO:
        1. Robust Error handling needs to be put in place to return logs & codes
            to the user for errors.
        2. Add capabilities for multiple directory or files within one function
            call for ease of use.            
    """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="greetings", description="Greet the user")
    async def greet(
        self, interaction: discord.Interaction, user: discord.Member, message: str
    ):
        await interaction.response.send_message(f"Hey {user.mention}! {message}")

    @app_commands.command(name="store-site", description="Store a site")
    async def storeSite(self, interaction: discord.Interaction, key: str, site: str):
        save_to_json(key, site)
        await interaction.response.send_message(f"Saved {site} to {key}")

    @app_commands.command(name="retrieve-site", description="Retrieve Site")
    async def retrieveSite(self, interaction: discord.Interaction, key: str):
        success, retrieved = retrieve_from_json(key)
        if success:
            site = retrieved
            await interaction.response.send_message(f"Site: {site}")
        else:
            error_message = retrieved
            await interaction.response.send_message(f"Error: {error_message}")

    @app_commands.command(name="list-sites", description="List sites from storage")
    async def listSites(self, interaction: discord.Interaction):
        success, result = list_sites()

        if success:
            response = "\n".join(result)
            await interaction.response.send_message(f"Stored sites:\n{response}")
        else:
            await interaction.response.send_message(f"Error: {result}")

    @app_commands.command(name="search-sites", description="Search for a stored site.")
    async def searchSites(self, interaction: discord.Interaction, query: str):
        success, result = search_sites(query)

        if success:
            response = "\n".join(result)
            await interaction.response.send_message(f"Stored Sites:\n{response}")
        else:
            await interaction.response.send_message(f"Error: {result}")

    @app_commands.command(
        name="search-fandom", description="Search Fandom for specifc items."
    )
    async def searchWiki(self, interaction: discord.Interaction, key: str, query: str):
        success, result = await get_fandom(key, query)

        if success:
            embed = discord.Embed(
                title=result["title"],
                description=result["summary"][:200] + "...",
                url=result["url"],
                color=0x00FF00,
            )
            if result["image"]:
                embed.set_image(url=result["image"])

            await interaction.response.send_message(embed=embed)

        else:
            print(f"Error Wiki command failed: {result}")
            await interaction.response.send_message(f"Error: {result}")


async def setup(bot):
    await bot.add_cog(FandomSearch(bot))
