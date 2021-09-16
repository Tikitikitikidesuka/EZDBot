from discord.ext import commands

from textchatmanager import TXTManager

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Test cog was loaded successfully")

    @commands.command()
    async def test(self, ctx):
        await TXTManager.send(ctx, "test", safe=False)

def setup(client):
    client.add_cog(Test(client))