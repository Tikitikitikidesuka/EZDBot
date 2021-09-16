from discord.ext.commands import Context

class VCManager():
    @classmethod
    async def join(cls, ctx:Context):
        if ctx.author.voice is not None:
            voiceChannel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voiceChannel.connect()
            else:
                await ctx.voice_client.move_to(voiceChannel)
            return True
        return False

    @classmethod
    async def leave(cls, ctx:Context):
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
            return True
        return False