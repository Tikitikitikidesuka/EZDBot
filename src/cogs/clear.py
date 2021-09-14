from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Clear cog was loaded successfully")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, arg='1'):
        if arg.isnumeric():
            await ctx.channel.purge(limit=int(arg) + 1)
        else:
            await ctx.send(arg + " is not a valid argument")

def setup(client):
    client.add_cog(Clear(client))