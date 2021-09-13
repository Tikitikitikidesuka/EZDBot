from discord.ext import commands

class RandomDraw(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("RandomDraw cog was loaded successfully")

    @commands.command()
    async def random(self, ctx):
        await ctx.send('Command isn\'t programmed yet :(')

def setup(client):
    client.add_cog(RandomDraw(client))