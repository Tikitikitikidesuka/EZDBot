import os
from dotenv import load_dotenv
from os.path import join, dirname

import discord
from discord.ext import commands, tasks


load_dotenv('./.env')
# Get Discord API token from .env file
DISCORD_TOKEN = os.getenv('discord_token')

# Create bot
client = commands.Bot(command_prefix='.', self_bot=False)

# Load all cogs in cogs directory
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

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


