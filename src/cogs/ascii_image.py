import os
from re import T
import requests
import PIL.Image
import validators
from discord.ext import commands

from textchatmanager import TXTManager


ASCII_CHARS = "░▒▓█"
IMAGE_SIZE = 44


def resizeImage(image, new_width=IMAGE_SIZE):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.5)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscaleImage(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ""
    for pixel in pixels:
        characters += ASCII_CHARS[int((len(ASCII_CHARS))*pixel/256)]
    return characters

def openImage(image):
    try:
        image = PIL.Image.open(image)
    except:
        return PIL.Image.NONE
    return image


class AsciiImage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("AsciiImage cog was loaded successfully")

    @commands.command()
    async def ascii(self, ctx, file_url=None):
        if not file_url: # If no url was sent
            if len(ctx.message.attachments) == 0: # If no file was sent
                await TXTManager.send(ctx, "Attach or link an image after the .ascii command", safe=False)
                return # Return because neither image nor url was sent
            # If file sent is valid get its url
            file_url = ctx.message.attachments[0].url
        elif not validators.url(file_url): # If url was sent and it is invalid
                await TXTManager.send(ctx, "Invalid image url", safe=False)
                return

        # Download the image
        img_data = requests.get(file_url).content
        with open('image.png', 'wb') as handler:
            handler.write(img_data)

        # Open the image
        image = openImage('image.png')
        if image:
            # Asciify the image
            new_image_data = pixels_to_ascii(grayscaleImage(resizeImage(image)))
            pixel_count = len(new_image_data)
            ascii_image = "```"
            for cntr in range(0, pixel_count, IMAGE_SIZE):
                ascii_image += new_image_data[cntr:(cntr+IMAGE_SIZE)] + "\n"
            ascii_image += '```'
            # Send the asciified image
            await TXTManager.deleteMessage(ctx)
            await TXTManager.send(ctx, ascii_image)
        else:
            await TXTManager.send(ctx, "Invalid image", safe=False)

        # Delete the image file
        os.remove('image.png')

def setup(client):
    client.add_cog(AsciiImage(client))