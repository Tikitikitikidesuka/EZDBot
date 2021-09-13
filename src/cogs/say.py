from discord.ext import commands
from discord.ext.commands.core import has_permissions

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Say cog was loaded successfully")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *text):
        response = ""
        for textfragment in text:
            response += textfragment + " "
        response = response[:-1]
        if len(response) < 2000:
            await ctx.message.delete()
            await ctx.send(response)
    
    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Missing permision to manage messages\nUse 'repeat' command instead")
    
    @commands.command()
    async def repeat(self, ctx, *text):
        response = ""
        for textfragment in text:
            response += textfragment + " "
        response = response[:-1]
        if len(response) < 2000:
            await ctx.send(response)

def setup(client):
    client.add_cog(Say(client))