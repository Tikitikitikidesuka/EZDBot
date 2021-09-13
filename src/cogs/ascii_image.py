import os
import requests
import PIL.Image
import validators
from discord.ext import commands

ASCII_CHARS = "█▓▒░"
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
        characters += ASCII_CHARS[int((pixel/255)*len(ASCII_CHARS))-1]
    return characters

class AsciiImage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("AsciiImage cog was loaded successfully")

    @commands.command()
    async def ascii(self, ctx, file_url=None):
        # Detect if image is attached, linked or missing
        if file_url is None:
            file_url = ctx.message.attachments[0].url
        elif validators.url(file_url):
            print("Image is link")
        else:  # If image isn't attached or linked method returns
            await ctx.send("Attach or link an image after the .ascii command")
            return

        # Download the image
        img_data = requests.get(file_url).content
        with open('image.png', 'wb') as handler:
            handler.write(img_data)

        # Open the image
        try:
            image = PIL.Image.open('image.png')
        except:
            print("WTF IMAGE")

        # Asciify the image
        new_image_data = pixels_to_ascii(grayscaleImage(resizeImage(image)))
        pixel_count = len(new_image_data)
        ascii_image = "```"
        for cntr in range(0, pixel_count, IMAGE_SIZE):
            ascii_image += new_image_data[cntr:(cntr+IMAGE_SIZE)] + "\n"
        ascii_image += '```'

        # Delete the image file
        os.remove('image.png')
        await ctx.message.delete()
        await ctx.send(ascii_image)

def setup(client):
    client.add_cog(AsciiImage(client))