# EZDBot
EZDBot is a Work in Progress general purpose Discord bot meant to be easily customized.
It comes with tools that make it a breeze to create a bot that fits perfectly on any server.
It has a modularized structure so that whatever feature needs to be implemented can be done so just by adding a file that specifies its desired behaviour.

## Features
At this time the bot has:
* An **audio manager** capable of playing audio files and YouTube videos on voice chat.
* A **text chat manager** capable of securely sending text messages on servers and DM's.
* A **voice chat manager** capable of moving the bot around a server's voice channels.

## Modules / Cogs
Some useful modules, also called cogs, come out of the box:
* [ascii_image](docs/cogs/clear.md): Produces ascii art from images sent
* [bonk](docs/cogs/bonk.md): Makes a gif of "Cheems" bonking a user's profile picture
* [pfp](docs/cogs/clear.md): Extracts a user's profile picture
* [play_audio](docs/cogs/clear.md): Plays a youtube video on voice chat
* [clear](docs/cogs/clear.md): Deletes the N previous sent messages in a channel
* [say](docs/cogs/say.md): Makes the bot say something

These cogs are being developed alongside the bot to test the managers that make the bot so versatile. They can easily be removed in case they are not needed just by moving their corresponding ```.py``` file out of the cogs folder located at ```src/cogs```.

Just as simple as removing any cog, adding a new one is as easy as placing the developed ```.py``` file in the cogs folder. A template cog comes in the docs with all the necesary code to make it work. Developing it after that just comes down to your python skills and your imagination.

## Configuring the bot
For the bot to work you must set ```discord_token``` on a ```.env``` file in the root dir of the project.
```
discord_token = "your_token"
```

## Dependencies
Python dependencies are specified in the requirements.txt file in the root folder.

The main library used to developed this project is [discord.py](https://github.com/Rapptz/discord.py) developed by [Rapptz](https://github.com/Rapptz).

## Authors
This project was developed by:
* SneakyGerbil
    * deesneakygerbil@gmail.com
    * [Itch.io](https://sneakygerbil.itch.io)
    * [YouTube](https://www.youtube.com/channel/UC4r_WrJ5SXjd10lFQdO3UyQ)
    * [GitHub](https://github.com/SneakyGerbil)

## License
Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg