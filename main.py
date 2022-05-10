
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
# TOKEN = 'ODUwMjQ4NTYxMDIyNTk5MTY5.GM2YDT.Sha6SzOp_WP-GdLjeYlWIM7ndbIXpouyc3mdpQ'

client = commands.Bot(command_prefix=".")
client.remove_command('help')

@client.event
async def on_ready():
    print("python bot is online")

@client.event
async def on_message(message):
    await client.process_commands(message)

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f"commands.{filename[:-3]}")

client.run(os.getenv('TOKEN'))