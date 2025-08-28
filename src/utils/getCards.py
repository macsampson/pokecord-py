import pokemontcgsdk as pokemon
import json
import random


async def getCards(card_set):
    common = await getCommon(card_set)
    uncommon = await getUncommon(card_set)
    rare = await getRare(card_set)
    cards = common + uncommon + rare

    return cards


async def getCommon(card_set):
    chosen = []
    try:
        data = pokemon.Card.where(q=f"set.id:{card_set} rarity:Common")
        for _ in range(6):
            chosen.append(random.choice(data))
        return chosen
    except Exception as e:
        print("error getting commons:", e)


async def getUncommon(card_set):
    chosen = []
    try:
        data = pokemon.Card.where(q=f"set.id:{card_set} rarity:Uncommon")
        for _ in range(3):
            chosen.append(random.choice(data))
        return chosen
    except Exception as e:
        print("error getting uncommons:", e)


async def getRare(card_set):
    chosen = []
    try:
        data = pokemon.Card.where(q=f"set.id:{card_set} rarity:Rare")
        for _ in range(1):
            chosen.append(random.choice(data))
        return chosen
    except Exception as e:
        print("error getting rares:", e)
