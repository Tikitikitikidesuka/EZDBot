import os
import sys
from dotenv import load_dotenv

import discord
from discord.ext import commands, tasks

# Add src directory to PATH
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
os.environ["ROOT_DIRECTORY"] = os.path.dirname(__file__)

load_dotenv('./.env')
# Get Discord API token from .env file
DISCORD_TOKEN = os.getenv('discord_token')

# Create bot
client = commands.Bot(command_prefix='.', self_bot=False)

# Load all cogs in cogs directory
for filename in os.listdir('src/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'src.cogs.{filename[:-3]}')

# Executed when bot is ready
@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="to you :3"
        )
    )
    print('Logged in as \"{0}\" ({0.id})'.format(client.user))

# Run the bot
client.run(DISCORD_TOKEN)



