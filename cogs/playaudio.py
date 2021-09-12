import discord
import validators
import youtube_dl
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
        voiceChannel = ctx.author.voice.channel
        if voiceChannel is not None:
            if ctx.voice_client is None:
                await voiceChannel.connect();
            else:
                await ctx.voice_client.move_to(voiceChannel)
        else:
            await ctx.send("You are not in a voice channel!")

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url : str):
        ctx.voice_client.stop()  # In case it was already playing something
        voiceClient = ctx.voice_client

        with youtube_dl.YoutubeDL(PlayAudio.YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **PlayAudio.FFMPEG_OPTIONS)
            voiceClient.play(source)

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