import validators
import youtube_dl

import discord
from discord.ext.commands import Context

class AudioManager():
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    YDL_OPTIONS = {
        'format': 'bestaudio',
        'verbose': False
    }

    @classmethod
    async def playAudio(cls, ctx:Context, url:str, allowLocal=False):
        if not ctx.voice_client is None:
            if validators.url(url):
                with youtube_dl.YoutubeDL(cls.YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(url, download=False)
                    url2 = info['formats'][0]['url']
                    source = await discord.FFmpegOpusAudio.from_probe(url2, **cls.FFMPEG_OPTIONS)
            elif allowLocal:
                print("Fetching: LOCAL/ " + url)
                source = discord.FFmpegOpusAudio(url)
            else:
                return False
            ctx.voice_client.play(source)
            return True
        else:
            print("It is none")
            return False
    
    @classmethod
    async def pauseAudio(cls, ctx:Context):
        await ctx.voice_client.pause()