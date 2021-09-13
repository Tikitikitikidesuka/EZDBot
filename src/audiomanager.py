import discord
import validators
import youtube_dl

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
    async def playAudio(cls, voiceClient, url:str, allowLocal=False):
        if validators.url(url):
            with youtube_dl.YoutubeDL(cls.YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **cls.FFMPEG_OPTIONS)
        elif not allowLocal:
            return False
        else:
            source = discord.FFmpegOpusAudio(url)
        voiceClient.play(source)
        return True