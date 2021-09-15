from discord.ext import commands
import discord

from textchatmanager import TXTManager

class PFP(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("PFP cog was loaded successfully")

    @commands.command()
    async def pfp(self, ctx):
        if len(ctx.message.mentions) > 0:
            await TXTManager.send(ctx.message.mentions[0].avatar_url)
        else:
            await ctx.send("Missing mention, usage:\npfp @user")
    
    @commands.command()
    async def pfp4me(self, ctx):
        if len(ctx.message.mentions) > 0:
            await TXTManager.dm(ctx.message.author, ctx.message.mentions[0].avatar_url)
            await TXTManager.deleteMessage(ctx)
        else:
            await ctx.send("Missing mention, usage:\npfp4me @user")

def setup(client):
    client.add_cog(PFP(client))