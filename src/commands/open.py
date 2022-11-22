from discord.ext import commands
import discord
from utils.getCards import getCards
from datetime import date
from utils.dictionaries import card_sets, rarityColors
import os


class Open(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(
        brief="command to open card packs",
        help=f"Set IDs: {os.linesep}{os.linesep.join(list(card_sets.keys()))}",
    )
    async def open(self, ctx, setId):
        print("i heard you")
        await ctx.send(f"Opening a {card_sets[setId][1]} pack!")
        try:
            cards = await getCards(card_sets[setId][0])
            for card in cards:
                embed_card = (
                    discord.Embed(
                        title=card.name,
                        description=card.flavorText if card.flavorText else "",
                        colour=rarityColors[card.rarity],
                    )
                    .set_image(url=card.images.large)
                    .set_author(
                        name=f"{ctx.message.author.name}'s {card.set.name} cards",
                        icon_url=ctx.message.author.avatar_url,
                    )
                    .add_field(name="Rarity", value=card.rarity)
                    .add_field(name="Artist", value=card.artist)
                    .set_footer(text=f"Pulled on {date.today().strftime('%B %d, %Y')}")
                )

                await ctx.send(embed=embed_card)

        except Exception as e:
            print("cant get cards.", e)
            await ctx.send("oh no, our api call...its broken")


def setup(client):
    client.add_cog(Open(client))
