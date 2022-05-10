from discord.ext import commands

class Open(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("open command is online")

    @commands.command()
    async def open(self,ctx):
        print("i heard you")
        await ctx.send("no open functionality yet")

def setup(client):
    client.add_cog(Open(client))