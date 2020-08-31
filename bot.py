import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

import os 




client = commands.Bot(command_prefix="$")

# Gets the discord token key
key_file = open("key.txt")
key = key_file.read()
key_file.close()


# Gets the help messages
help_file = open("data/help.txt")
help_info = help_file.read()
help_file.close()




@client.event
async def on_ready():

    activity = discord.Game("$help")
    await client.change_presence(status=discord.Status.online, activity=activity)




"""
@client.command(
    name='tlh',
    description = 'Plays hymns from the tlh ')
async def tlh(ctx, hymn_index):
    #Grab user info
    user = ctx.message.author
    voice_channel = user.voice.channel
    

    #Check if user is in a channel
    if(voice_channel != None):
        vc = await voice_channel.connect()

        vc.play(discord.FFmpegPCMAudio('http://lutherantacoma.com/hymns/001.mp3'), after=lambda e: print('done', e))
    else:
        await ctx.send("Join a voice channel first.")
"""

for filename in os.listdir('./cogs'):
    if(filename.endswith('.py')):
        client.load_extension(f'cogs.{filename[:-3]}')


if key == "" or key == None:
    print("There is no key")
else:
    client.run(key)
