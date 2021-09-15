from discord import User, Asset, DMChannel


MAX_MESSAGE_LEN = 2000

class TXTManager():
    # Safe way of sending messages as response on channel
    @classmethod
    async def send(cls, ctx, message):
        if isinstance(message, str) and len(message) <= MAX_MESSAGE_LEN:
            await ctx.send(message)
            return True
        return False

    # Safe way of sending dm messages
    @classmethod
    async def dm(cls, user:User, message):
        if isinstance(message, str):
            if len(message) <= MAX_MESSAGE_LEN:
                await user.send(message)
                return True
        elif isinstance(message, Asset):
            await user.send(message)
            return True
        return False
    
    # Safe way of deleting messages on servers
    @classmethod
    async def deleteMessage(cls, ctx):
        if not isinstance(ctx.channel, DMChannel):
            await ctx.message.delete()
            return True
        return False