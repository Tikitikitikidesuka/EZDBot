from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping cog was loaded successfully")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("`Ping: " + str(round(self.client.latency * 1000)) + " ms`")

def setup(client):
    client.add_cog(Ping(client))