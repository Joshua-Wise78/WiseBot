import discord
import logging
import os
import sys
import traceback
from discord.ext import commands
from dotenv import load_dotenv

from server.connection import ConnectionManager

load_dotenv()
try:
    TOKEN = os.environ["DISCORD_TOKEN"]
    ID = int(os.environ["GUILD_ID"])
except KeyError as e:
    print(f"Missing environment variable {e}")
    sys.exit(1)
except ValueError:
    print(f"Error: GUILD_ID is not a valid number")
    sys.exit(1)

GUILD_ID = discord.Object(id=ID)

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def setup_hook():
    print("Initializing server connections...")
    bot.connections = ConnectionManager()
    await bot.connections.connect_all()

bot.setup_hook = setup_hook

initial_extensions = ["cogs.fandomSearch", "cogs.immich", "server.status"]

@bot.event
async def on_ready():
    print(f"{bot.user} connected to Discord")

    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f"Extension loaded: {extension}")
        except Exception as e:
            print(f"Failed to load extension: {extension}. Reason: {e}")
            traceback.print_exc()

    try:
        bot.tree.copy_global_to(guild=GUILD_ID)
        await bot.tree.sync(guild=GUILD_ID)
        print("Synced command(s) to server")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    bot.run(TOKEN, log_handler=handler)
