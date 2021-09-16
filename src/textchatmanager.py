from discord import User, Asset, DMChannel


MAX_MESSAGE_LEN = 2000

class TXTManager():
    # Safe way of sending messages as response on channel
    @classmethod
    async def send(cls, ctx, message, safe=True):
        if (not safe) or (isinstance(message, str) and len(message) <= MAX_MESSAGE_LEN) or isinstance(message, Asset):
            await ctx.send(message)
            return True
        return False

    # Safe way of sending dm messages
    @classmethod
    async def dm(cls, user:User, message, safe=True):
        if (not safe) or (isinstance(message, str) and len(message) <= MAX_MESSAGE_LEN) or isinstance(message, Asset):
            await user.send(message)
            return True
        return False
    
    # Safe way of deleting messages on servers
    @classmethod
    async def deleteMessage(cls, ctx):
        if not isinstance(ctx.channel, DMChannel) and ctx.me.guild_permissions.manage_messages:
            await ctx.message.delete()
            return True
        return False
        