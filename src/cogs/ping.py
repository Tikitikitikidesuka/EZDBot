from discord.ext import commands

from textchatmanager import TXTManager

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping cog was loaded successfully")

    @commands.command()
    async def ping(self, ctx):
        await TXTManager.send("Ping: " + str(round(self.client.latency * 1000)) + " ms")

def setup(client):
    client.add_cog(Ping(client))