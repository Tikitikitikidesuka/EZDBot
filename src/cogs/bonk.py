import os
import requests
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFilter

from cogs.ascii_image import resizeImage

class Bonk(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bonk cog was loaded successfully")

    @commands.command()
    async def bonk(self, ctx):
        # Get mentioned user's pfp image url
        pfp_url = ctx.message.mentions[0].avatar_url
        # Download the image
        img_data = requests.get(pfp_url).content
        with open('pfp.png', 'wb') as handler:
            handler.write(img_data)

        # Open the images
        pfpImage = Image.open('pfp.png')
        cheemsImage = Image.open(os.path.join(os.environ["ROOT_DIRECTORY"], 'assets', 'images', 'bonk', 'Bonk0.png'))

        # Make pfp the right size
        pfpImage = pfpImage.resize((180, 180))
        finalImage = Image.Image.paste(cheemsImage, pfpImage, (630, 290))

        # Save the edited image
        cheemsImage.save('final.png')

        

def setup(client):
    client.add_cog(Bonk(client))