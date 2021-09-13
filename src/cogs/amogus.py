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
        voiceClient = ctx.voice_client
        voiceClient.stop()  # In case it was already playing something

        # Check the sender is in a voice channel
        if ctx.author.voice is not None:
            # Move to the senders voice channel
            voiceChannel = ctx.author.voice.channel
            if voiceClient is None:
                await voiceChannel.connect();
            else:
                await voiceClient.move_to(voiceChannel)
            # Play the sound
            await AudioManager.playAudio(ctx.voice_client, AMOGUS_SOUND_FILE, allowLocal=True)
            await ctx.message.delete()
        else:
            await ctx.send("You are not in a voice channel!")

def setup(client):
    client.add_cog(Amogus(client))