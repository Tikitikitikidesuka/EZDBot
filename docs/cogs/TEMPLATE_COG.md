# Template Cog

```python
from discord.ext import commands

class Template(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Executed when cog is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print("Template cog was loaded successfully")

    # Command example
    @commands.command()
    async def example(self, ctx):
        await ctx.send('example')

# Load cog
def setup(client):
    client.add_cog(Template(client))
```