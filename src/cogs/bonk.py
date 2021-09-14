import os
import discord
import requests
from PIL import Image
from random import randint
from discord.ext import commands


CIRCLE_MASK_DIR = os.path.join(os.environ["ROOT_DIRECTORY"], 'assets', 'images', 'bonk', 'CircleMask.png')
CHEEMS_IMAGE_DIR = os.path.join(os.environ["ROOT_DIRECTORY"], 'assets', 'images', 'bonk', 'Bonk') # It just needs the frame number and .png
BACKGROUND_IMAGE_DIR = os.path.join(os.environ["ROOT_DIRECTORY"], 'assets', 'images', 'bonk', 'Background') # It just needs the bg number and .png

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
        pfpMask = Image.open(CIRCLE_MASK_DIR)
        backgroundImage = Image.open(BACKGROUND_IMAGE_DIR + str(randint(0, 5)) + '.png')
        cheemsImages = [Image.open(CHEEMS_IMAGE_DIR + '0.png'), Image.open(CHEEMS_IMAGE_DIR + '1.png')]
        width = cheemsImages[0].width
        height = cheemsImages[0].height

        # Make pfp the right size
        pfpImage = pfpImage.resize((180, 180))
        # Make pfp round
        pfpImage.putalpha(pfpMask)

        editedFrames = []
        for frame in range(2):
            # Layer the images
            editedFrames.append(Image.new('RGBA', (width, height), color=(0,0,0,0)))
            editedFrames[frame].paste(backgroundImage)
            editedFrames[frame].paste(pfpImage, (635, 290), pfpImage)
            editedFrames[frame].paste(cheemsImages[frame], (0, 0), cheemsImages[frame])

        # Save the gif
        editedFrames[0].save('final.gif', save_all=True, format='GIF', loop=0, duration=250, append_images=editedFrames[1:])

        # Send the image
        with open('final.gif', 'rb') as finalImageFile:
            finalImageDiscord = discord.File(finalImageFile)
            await ctx.send(file=finalImageDiscord)

        

def setup(client):
    client.add_cog(Bonk(client))