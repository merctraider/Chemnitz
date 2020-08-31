import discord 
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

from utils.roman_numbers import roman_numbers


class BookOfConcord(commands.Cog):
    


    def __init__(self, client):
        self.client = client

    
    def EmbedBlock(self, header, text):
        return discord.Embed(title=header, description=text, color=0x0080FF)


    #Commands
    @commands.command(name="AC", description="Retrieve a quote from the Augsburg Confession")
    async def ac(self, ctx, *args):
        html_ac = requests.get("http://bookofconcord.org/augsburgconfession.php")
        soup = BeautifulSoup(html_ac.content, "html.parser")
        criteria = None 
        header = "Augsburg Confession"
        text = ""
        #Check how many arguments
        if len(args) == 1:
            query = args[0]
            #Check if it is a number
            if IsNumber(args[0]):
                #Check if it is an integer
                if RepresentsInt(query):
                    article_ID = query
                    text = await BuildText(self, ctx, soup, query)
                else:
                    #It is a float (e.g. 1.1) 
                    criteria = '#article'+ str(query)
                    text = ScrapeText(soup, criteria)
                    article_ID = query[:-2]

            else:
                article_ID = roman_numbers.romanToInt(self, args[0])
                await ctx.send(str(article_ID))
                #It is a letter 
                try:
                    name_to_find = str(args[0]).lower()
                    await ctx.send(name_to_find)
                    a_tag = soup.find(name=name_to_find)
                    await ctx.send(str(a_tag.next_sibling))
                    header = a_tag.next_sibling.strip()
                except:
                    header = "Augsburg Confession Article " + str(article_ID)
                    
                text = await BuildText(self, ctx, soup, article_ID)
        
        elif len(args) == 2:
            pass
        else:
            await ctx.send("$AC ``<article number> <paragraph number>``  E.g. `$AC IV 1` or `$AC 4 1`")
            await ctx.send("$AC ``<article number>``  E.g. `$AC IV` or `$AC 4`")
            await ctx.send ("$AC ``<article number>.<paragraph number>``  E.g. `$AC 4.1`")

        


        if len(text) > 0:
            e = BookOfConcord.EmbedBlock(self, header, text)
            await ctx.send(embed=e)



    """
    @commands.command(name="AC", description="Gets something from the Augsburg confession")
    async def ac(self, ctx, query):

        html_ac = requests.get("http://bookofconcord.org/augsburgconfession.php")
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
                    e = BookOfConcord.EmbedBlock(self, header, text)
                    await ctx.send(embed=e)
                    text = ""
        else:
            text = ScrapeText(soup, criteria)
            text.replace("\n", "")
        if len(text) > 0:
            e = BookOfConcord.EmbedBlock(self, header, text)
            await ctx.send(embed=e)
        """

async def BuildText(self, ctx, soup, query):

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
        try:
            text += " " + ScrapeText(soup, x_crit)            
        except:
            await ctx.send("Error in finding" + x_crit)
        
        if len(text) > 1500:

            e = BookOfConcord.EmbedBlock(self, "Article " + str(query), text)
            await ctx.send(embed=e)
            text = ""
    return text




def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def ScrapeText(soup, criteria):
    element = soup.find(href=criteria)
    return element.next_sibling.strip()

def IsNumber(s):
    return any(char.isdigit() for char in s)
    


def setup(client):
    client.add_cog(BookOfConcord(client))
    