from discord.ext import commands

class PFP(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("PFP cog was loaded successfully")

    @commands.command()
    async def pfp(self, ctx):
        print(ctx.message.mentions[0].id)
        await ctx.send(ctx.message.mentions[0].avatar_url)
        #await ctx.send(ctx.message.author.mention())

def setup(client):
    client.add_cog(PFP(client))