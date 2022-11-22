import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from cogwatch import Watcher


load_dotenv()
# TOKEN = 'ODUwMjQ4NTYxMDIyNTk5MTY5.GM2YDT.Sha6SzOp_WP-GdLjeYlWIM7ndbIXpouyc3mdpQ'

client = commands.Bot(command_prefix=".")
# client.remove_command('help')


@client.event
async def on_ready():
    print("python bot is online")
    watcher = Watcher(client, path="commands", preload=True)
    await watcher.start()


@client.event
async def on_message(message):
    await client.process_commands(message)


# load all the bot commands
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        try:
            client.load_extension(f"commands.{filename[:-3]}")
            print(filename[:-3].upper(), "command is online")
        except Exception as e:
            print("Issue loading", filename[:-3].upper(), "command", e)

client.run(os.getenv("TOKEN"))
