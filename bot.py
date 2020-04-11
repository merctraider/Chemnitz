import discord
from discord.ext import commands
import youtube_dl
from bs4 import BeautifulSoup
import requests


client = commands.Bot(command_prefix="$")

# Gets the discord token key
key_file = open("key.txt")
key = key_file.read()
key_file.close()


# Gets the help messages
help_file = open("help.txt")
help_info = help_file.read()
help_file.close()

# Gets the websites
html_ac = requests.get("http://bookofconcord.org/augsburgconfession.php")


@client.event
async def on_ready():

    activity = discord.Game("$help")
    await client.change_presence(status=discord.Status.online, activity=activity)


def EmbedBlock(header, text):
    return discord.Embed(title=header, description=text, color=0x0080FF)


@client.command(name="AC", description="Gets something from the Augsburg confession")
async def ac(ctx, query):
    soup = BeautifulSoup(html_ac.content, "html.parser")
    criteria = "#article" + str(query)
    header = "Augsburg Confession Article " + str(query)
    if RepresentsInt(query):
        ac_article_lengths = [
            24,
            6,
            3,
            6,
            3,
            4,
            3,
            2,
            3,
            3,
            2,
            2,
            10,
            3,
            1,
            3,
            7,
            5,
            9,
            1,
            40,
            14,
            12,
            26,
            40,
            13,
            45,
            61,
            78,
            17,
        ]
        text = ""
        for x in range(1, ac_article_lengths[int(query)] + 1):
            x_crit = "#article" + str(query) + "." + str(x)
            text += " " + ScrapeText(soup, x_crit)
            if len(text) > 1500:
                e = EmbedBlock(header, text)
                await ctx.send(embed=e)
                text = ""
    else:
        text = ScrapeText(soup, criteria)
        text.replace("\n", "")
    if len(text) > 0:
        e = EmbedBlock(header, text)
        await ctx.send(embed=e)


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def ScrapeText(soup, criteria):
    element = soup.find(href=criteria)
    return element.next_sibling.strip()


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


if key == "" or key == None:
    print("There is no key")
else:
    client.run(key)
