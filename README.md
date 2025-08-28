# Pokecord Python Bot

A Discord bot that simulates opening Pokemon trading card packs using the Pokemon TCG API.

## Features

- **Pack Opening**: Use `.open <set>` to open booster packs from various Pokemon TCG sets
- **Card Display**: Cards are displayed as rich Discord embeds with artwork, rarity colors, and metadata
- **Multiple Sets**: Support for 125+ Pokemon TCG sets from Base Set to Battle Styles
- **Realistic Distribution**: Each pack contains 6 common, 3 uncommon, and 1 rare card

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv env`
3. Activate it: `source env/bin/activate` (Linux/Mac) or `env\Scripts\activate` (Windows)
4. Install dependencies: `pip install discord.py pokemontcgsdk python-dotenv cogwatch`
5. Create a `.env` file in the root directory with your Discord bot token:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```
6. Run the bot: `python src/main.py`

## Usage

- `.open base` - Opens a Base Set booster pack
- `.open jungle` - Opens a Jungle booster pack
- `.help` - Shows available commands

Use `.open` with any set ID from the supported list. Popular sets include: `base`, `jungle`, `fossil`, `teamrocket`, `neogenesis`, `xy`, `sunandmoon`, `swordandshield`.

## Architecture

Built with Discord.py using the cogs system for modular commands. Card data is fetched from the Pokemon TCG API and displayed with rarity-appropriate colors and formatting.