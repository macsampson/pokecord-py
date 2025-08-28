from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        # print("help command is online")
        pass

    @commands.command()
    async def help(self, ctx):
        print("i heard you")
        await ctx.send("no elp")


def setup(client):
    client.add_cog(Help(client))
