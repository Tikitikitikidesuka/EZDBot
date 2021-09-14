import os
from posix import listdir
import discord
import requests
from PIL import Image
from random import choice
from discord.ext import commands


CIRCLE_MASK_DIR = os.path.join(os.environ["ROOT_DIRECTORY"], 'assets', 'images', 'bonk', 'CircleMask.png')
CHEEMS_IMAGE_DIR = os.path.join(os.environ["ROOT_DIRECTORY"], 'assets', 'images', 'bonk', 'Bonk') # It just needs the frame number and .png
BACKGROUND_IMAGE_DIR = os.path.join(os.environ["ROOT_DIRECTORY"], 'assets', 'images', 'bonk', 'backgrounds') # It just needs the bg number and .png


def makeImageRound(image:Image, mask:Image):
    if image.mode == 'RGBA':
        if image.width == mask.width and image.height == mask.height:
            for x in range(image.width):
                for y in range(image.height):
                    mkPixel = mask.getpixel((x, y))
                    imPixel = image.getpixel((x,y))
                    imPixel = (imPixel[0], imPixel[1], imPixel[2], min(mkPixel, imPixel[3]))
                    image.putpixel((x,y), imPixel)
            return True
    else:
        print("Image on makeImageRound has to be RGBA")
    return False
                

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
        pfpImage = Image.open('pfp.png').convert('RGBA')
        pfpMask = Image.open(CIRCLE_MASK_DIR)
        backgroundImage = Image.open(os.path.join(BACKGROUND_IMAGE_DIR, file))#choice(listdir(BACKGROUND_IMAGE_DIR))))
        cheemsImages = [Image.open(CHEEMS_IMAGE_DIR + '0.png'), Image.open(CHEEMS_IMAGE_DIR + '1.png')]
        width = cheemsImages[0].width
        height = cheemsImages[0].height

        # Set editing variables
        pfpSize = 180
        squishDist = 10
        pfpPosX = 635
        pfpPosY = 290
        # Make pfp the right size
        pfpImage = pfpImage.resize((pfpSize, pfpSize))
        # Make pfp round
        makeImageRound(pfpImage, pfpMask)
        # Squish pfp for the second frame
        squishedPfpImage = pfpImage.resize((pfpSize, pfpSize - squishDist))
                
        # Edit frames
        editedFrames = []
        # Edit first frame
        editedFrames.append(Image.new('RGBA', (width, height), color=(0,0,0,0)))
        editedFrames[0].paste(backgroundImage)
        editedFrames[0].paste(pfpImage, (pfpPosX, pfpPosY), pfpImage)
        editedFrames[0].paste(cheemsImages[0], (0, 0), cheemsImages[0])
        # Edit second frame
        editedFrames.append(Image.new('RGBA', (width, height), color=(0,0,0,0)))
        editedFrames[1].paste(backgroundImage)
        editedFrames[1].paste(squishedPfpImage, (pfpPosX, pfpPosY + squishDist), squishedPfpImage)
        editedFrames[1].paste(cheemsImages[1], (0, 0), cheemsImages[1])
        
        # Save the gif
        editedFrames[0].save('final.gif', save_all=True, format='GIF', loop=0, duration=300, append_images=[editedFrames[1], editedFrames[1]])

        # Send the image
        with open('final.gif', 'rb') as finalImageFile:
            finalImageDiscord = discord.File(finalImageFile)
            await ctx.send(file=finalImageDiscord)

        
def setup(client):
    client.add_cog(Bonk(client))