from discord.ext import commands

from textchatmanager import TXTManager

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Clear cog was loaded successfully")

    @commands.command()
    async def clear(self, ctx, arg='1'):
        if arg.isnumeric():
            if not await TXTManager.deletePrevMessages(ctx, int(arg) +1):
                await TXTManager.send(ctx, "Missing permissions to manage messages")
        else:
            await TXTManager.send(ctx, arg + " is not a valid argument", safe=False)

def setup(client):
    client.add_cog(Clear(client))