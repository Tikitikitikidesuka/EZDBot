from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Clear cog was loaded successfully")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount='1'):
        if amount == 'all':
            await ctx.channel.purge()
        elif amount.isnumeric():
            await ctx.channel.purge(limit=int(amount) + 1)
        else:
            await ctx.send(amount + " is not a valid argument")

def setup(client):
    client.add_cog(Clear(client))