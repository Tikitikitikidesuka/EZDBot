from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Say cog was loaded successfully")

    @commands.command()
    async def say(self, ctx, *text):
        response = ""
        for textfragment in text:
            response += textfragment + " "
        response = response[:-1]
        if len(response) < 2000:
            await ctx.message.delete()
            await ctx.send(response)

def setup(client):
    client.add_cog(Say(client))