from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Say cog was loaded successfully")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def uSay(self, ctx, *text):
        response = ""
        for textfragment in text:
            response += textfragment + " "
        response = response[:-1]
        if len(response) < 2000:
            await ctx.message.delete()
            await ctx.send(response)
        else:
            await ctx.send("Message can't be longer than 2000 characters")

    @uSay.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Missing permissions")

    @commands.command()
    async def say(self, ctx, *text):
        response = ""
        for textfragment in text:
            response += textfragment + " "
        response = response[:-1]
        if len(response) < 2000:
            await ctx.send(response)
        else:
            await ctx.send("Message can't be longer than 2000 characters")

def setup(client):
    client.add_cog(Say(client))