import os

from discord.ext import commands
from audiomanager import AudioManager

AMOGUS_SOUND_FILE = os.path.join(os.environ["ROOT_DIRECTORY"], 'assets', 'amogus.mp3')

class Amogus(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Amogus cog was loaded successfully")

    @commands.command()
    async def amogus(self, ctx):
        await ctx.message.delete()
        await ctx.send(AMOGUS_SOUND_FILE)
        await AudioManager.playAudio(ctx.voice_client, AMOGUS_SOUND_FILE, allowLocal=True)

def setup(client):
    client.add_cog(Amogus(client))