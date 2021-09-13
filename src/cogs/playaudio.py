from audiomanager import AudioManager
from discord.ext import commands

class PlayAudio(commands.Cog):
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    YDL_OPTIONS = {
        'format': 'bestaudio',
        'verbose': False
    }

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("PlayAudio cog was loaded successfully")

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is not None:
            voiceChannel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voiceChannel.connect();
            else:
                await ctx.voice_client.move_to(voiceChannel)
        else:
            await ctx.send("You are not in a voice channel!")

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("Chill, dude, I'm not even in!")

    @commands.command()
    async def play(self, ctx, url : str):
        if ctx.voice_client is None:
            await self.join(ctx)

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
            await AudioManager.playAudio(voiceClient, url)
        else:
            await ctx.send("You are not in a voice channel!")

    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused")

    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("Resumed")


def setup(client):
    client.add_cog(PlayAudio(client))