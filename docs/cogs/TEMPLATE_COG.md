# Template Cog

```python
from discord.ext import commands

class Template(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Template cog was loaded successfully")

    @commands.command()
    async def example(self, ctx):
        await ctx.send('example')

def setup(client):
    client.add_cog(Template(client))
```