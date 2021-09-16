from discord.ext import commands
from discord.ext.commands.core import has_permissions

from textchatmanager import TXTManager


class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Say cog was loaded successfully")

    @staticmethod
    def joinStrings(text):
        finalStr = ""
        for textfragment in text[:-1]:
            finalStr += textfragment + " "
        return finalStr + text[-1]

    @commands.command()
    async def say(self, ctx, *text):
        if len(text) > 0:
            if not await TXTManager.deleteMessage(ctx):
                await TXTManager.send(ctx, "Missing permision to manage messages\nUse 'repeat' command instead", safe=False)
            else:
                await TXTManager.send(ctx, self.joinStrings(text))
        else:
            await TXTManager.send(ctx, "Missing text to say\nUsage: say text", safe=False)
    
    @commands.command()
    async def repeat(self, ctx, *text):
        if len(text) > 0:
            await TXTManager.send(ctx, self.joinStrings(text))
        else:
            await TXTManager.send(ctx, "Missing text to say\nUsage: say text", safe=False)

def setup(client):
    client.add_cog(Say(client))