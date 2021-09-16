from discord.ext import commands
from audiomanager import AudioManager
from textchatmanager import TXTManager
from voicechatmanager import VCManager


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
        if not await VCManager.join(ctx):
            await TXTManager.send(ctx, "You are not in a voice channel")

    @commands.command()
    async def leave(self, ctx):
        if not await VCManager.leave(ctx):
            await TXTManager.send(ctx, "I'm not in a voice channel")

    @commands.command()
    async def play(self, ctx, url : str):
        if await VCManager.join(ctx):
            if not await AudioManager.playAudio(ctx, url):
                await TXTManager.send(ctx, "Invalid audio source", safe=False)
        else:
            await TXTManager.send(ctx, "You are not in a voice channel!", safe=False)

    @commands.command()
    async def pause(self, ctx):
        if await AudioManager.pauseAudio(ctx):
            await TXTManager.send(ctx, "Paused", safe=False)
        else:
            await TXTManager.send(ctx, "No audio to pause", safe=False)

    @commands.command()
    async def resume(self, ctx):
        if await AudioManager.resumeAudio(ctx):
            await TXTManager.send(ctx,"Resumed", safe=False)
        else:
            await TXTManager.send(ctx,"No audio to resume", safe=False)

    @commands.command()
    async def stop(self, ctx):
        await AudioManager.stopAudio(ctx)
        await TXTManager.send(ctx,"Stopped", safe=False)

def setup(client):
    client.add_cog(PlayAudio(client))