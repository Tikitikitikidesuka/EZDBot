import os
import sys
from requests import get
from dotenv import load_dotenv

import discord
from discord.ext import commands


def exitVerbose():
    print("Exiting the program...")
    sys.exit(1)

# Add src directory to PATH
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
os.environ["ROOT_DIRECTORY"] = os.path.dirname(__file__)

#Check if .env file exists
envPath = os.path.join(os.environ["ROOT_DIRECTORY"], '.env')
if not os.path.isfile(envPath):
    print("Missing .env file required for connection.")
    exitVerbose()

# Get Discord API token from .env file
load_dotenv(envPath)
DISCORD_TOKEN = os.getenv('discord_token')
#Check if the token was in the .env file
if not DISCORD_TOKEN:
    print(
        "discord_token enviroment variable missing.\n"
        "Add the following line in the .env file:\n\n"
        "discord_token = \"your_token\"\n\n"
        "replacing your_token with your bot\'s token."
    )
    exitVerbose()

# Create bot
client = commands.Bot(command_prefix='.', self_bot=False)

# Load all cogs in cogs directory
for filename in os.listdir(os.path.join(os.environ["ROOT_DIRECTORY"],'src', 'cogs')):
    if filename.endswith('.py'):
        client.load_extension(f'src.cogs.{filename[:-3]}')

# Executed when bot is ready
@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="you :3"
        )
    )
    print('Logged in as \"{0}\" ({0.id})'.format(client.user))

# Run the bot
try:
    client.run(DISCORD_TOKEN)
except:
    print("Login error, check that discord_token in .env file is correct.")
    exitVerbose()