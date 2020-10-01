import discord 
from discord.ext import commands
from bs4 import BeautifulSoup
import requests


class TLH(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Commands
    @commands.command(name="matins", description="Play the accompaniment from the rubrics")
    async def matins(self, ctx, *arg):
        if(arg[0] == "versicle" or arg[0] == "1"):
            await ctx.send("O Lord, open thou my lips")
            await ctx.send("**And my mouth shall show forth Thy praise**")
            await PlaySound(ctx, "tlh/matins-versicle.mp3")
        elif (arg[0] == "gloria" or arg[0] == "2"):
            await ctx.send("Make haste, O God, to deliver me.")
            await ctx.send ("**Make haste to help me, O Lord**")
            e = discord.Embed(title="Gloria Patri", description = "Glory be to the Father and to the Son: \n and to the Holy Ghost\n\n As it was in the beginning, is now, and ever shall be: \n world without end. Amen.", color=0x0080FF)
            await ctx.send(embed=e)
            await PlaySound(ctx, "tlh/matins-gloria-patri.mp3")
        elif (arg[0] == "invitatory" or arg[0] == "3"):
            await ctx.send("Oh come, let us worship the Lord")
            await ctx.send("**For He is our Maker.**")
            await PlaySound(ctx,"tlh/matins-invitatory.mp3")
        elif (arg[0] == "venite" or arg[0] =="4"):
            e = discord.Embed (title="The Venite", description= "O come let us sing unto the Lord\n Let us make a joyful noise to the Rock of our salvation.\n Let us come before His presence with thanksgiving;\n And make a joyful noise unto Him with psalms.\n For the Lord is a great God\n And a great King above all gods.\n In His hand are the deep places of the earth;\n The strength of the hills is His also \nThe sea is His, and He made it;\n And His hands formed the dry land.\n Oh, come let us worship and bow down;\n Let us kneel before the Lord our maker\n For He is our God And we are the people of His pasture\n And the sheep of His hand.\n Glory be to the Father and to the Son\n And to the Holy Ghost\n As it was in the beginning, is now,\n And ever shall be; world without end. Amen.", color=0x0080FF)
            await ctx.send(embed=e)
            await PlaySound(ctx, "tlh/matins-venite.mp3")
        elif (arg[0] == "lection" or arg[0] == "5"):
            await ctx.send("But Thou, O Lord, have mercy upon us")
            await ctx.send("**Thanks be to Thee, O Lord!**")
            await PlaySound(ctx,"tlh/matins-lection-response.mp3")
        elif (arg[0] == "tedeum" or arg[0] == "6"):
            e = discord.Embed (title="The Te Deum Laudamus", description= "We praise Thee O God, we acknowledge Thee to be the Lord.\n All the earth doth worship Thee, the Father Everlasting.\n To Thee all the angels cry aloud, the heavens and all the powers therein;\n To Thee cherubim and seraphim continually do cry;\n Holy, holy, holy, Lord God of Sabaoth;\n Heaven and earth are full of the majesty of Thy glory.\n The glorious company of the Apostles praise Thee\n The goodly fellowship of the prophets praise Thee;\n The noble army of martyrs praise Thee;\n The holy Church though all the world doth acknowledge Thee;\n The Father of an infinite majesty; Thine adorable true and only Son,\n Also the Holy Ghost, the Comforter.\n Thou art the King of Glory, O Christ.\n Thou are the everlasting Son of the Father.\n When Thou tookest upon Thee to deliver man;\n Thou didst humble Thyself to be born of a virgin.\n When Thou hadst overcome the sharpness of death,\n Thou didst open the kingdom of heaven to all believers.\n Thou sittest at the right hand of God\n In the glory of the Father.\n We believe that thou shalt come To be our judge.\n We therefore pray Thee to help Thy servants,\n Whom Thou hast redeemed with Thy precious blood.\n Make them to be numbered with Thy saints In glory everlasting.\n O Lord, save Thy people and bless Thine heritage.\n Govern them and lift them up forever.\n Day by day we magnify Thee,\n And we worship Thy name ever, world without end.\n Vouchsafe, O Lord, to keep us this day without sin,\n O Lord have mercy upon us, have mercy upon us,\n O Lord, let Thy mercy be upon us, as our trust is in Thee.\n O Lord, in Thee have I trusted; let me never be confounded.", color=0x0080FF)
            await ctx.send(embed=e)
            await PlaySound(ctx, "tlh/matins-te-deum.mp3")
        elif (arg[0] == "kyrie" or arg[0] == "7"):
            e = discord.Embed (title="The Kyrie", description= "Lord, have mercy upon us \n Christ, have mercy upon us\n Lord, have mercy upon us", color=0x0080FF)
            await ctx.send(embed=e)
            await PlaySound(ctx, "tlh/matins-kyrie.mp3")
        elif (arg[0] == "salutation" or arg[0] == "8"):
            await ctx.send("The Lord be with you.")
            await ctx.send("**And with thy spirit**")
            await PlaySound(ctx, "tlh/matins-salutation.mp3")
        elif (arg[0] == "amen" or arg[0] == "9"):
            await ctx.send("**Amen**")
            await PlaySound(ctx, "tlh/matins-collect-amen.mp3")
        elif (arg[0] == "benedicamus" or arg[0] == "10"):
            await ctx.send("Bless we the Lord.")
            await ctx.send("**Thanks be to God.**")
            await PlaySound(ctx, "tlh/matins-benedicamus.mp3")
        elif (arg[0] == "benediction" or arg[0] == "11"):
            await ctx.send("The grace of our Lord Jesus Christ and the love of God and the communion of the Holy Ghost be with you all.")
            await ctx.send("**Amen.**")
            await PlaySound(ctx, "tlh/matins-benediction.mp3")
        elif (arg[0] == "magnificat"):
            e = discord.Embed (title="The Magnificat", description= "My soul doth magnify the Lord,\n and my spirit hath rejoiced in God, my Savior.\n\n For He hath regarded\n the low estate of His handmaiden:\n\n for, behold, from henceforth\n all generations shall call me blessed.\n\n For He that is mighty hath done to me great things,\n and holy is His name.\n\n And His mercy is on them that fear Him\n from generation to generation.\n\n He hath showed strength with His arm\n He hath scattered the proud in the imagination of their hearts.\n\n He hath put down the mighty from their seats,\n and exalted them of low degree. \n\n He hath filled the hungry with good things,\n and the rich He hath sent empty away.\n\n He hath holpen His servant Israel,in remembrance of His mercy,\n as He spake to our fathers, to Abraham, and to his seed forever.;", color=0x0080FF)
            await ctx.send(embed=e)
            e = discord.Embed(title="Gloria Patri", description = "Glory be to the Father and to the Son: \n and to the Holy Ghost\n\n As it was in the beginning, is now, and ever shall be: \n world without end. Amen.", color=0x0080FF)
            await ctx.send(embed=e)
            await PlaySound(ctx, "tlh/matins-magnificat.mp3")
        
    @commands.command(name="tlh", description="Get the lyrics to a hymn.")
    async def tlh(self, ctx, *arg):
        if(RepresentsInt(arg[0])):
            hymnID = "{0:03}".format(int(arg[0]))
            html_link = "https://clcgracelutheranchurch.org/fridley/hymns/tlh/tlh" + hymnID + ".htm"
            print("Trying to retrieve " + html_link)
            try:
                html_hymn = requests.get(html_link)
                print(html_hymn.status_code)
                soup = BeautifulSoup(html_hymn.content, "html.parser")
                
                await BuildHymnText(ctx, soup)
                
                    
                
            except:
                await ctx.send("Please input a valid hymn.")
        
        
        
        
        





#Join a discord channel to play a sound from the library
async def PlaySound(ctx, source):
    #Grab user info
    user = ctx.message.author
    voice_channel = user.voice.channel
    vc = ctx.voice_client 
    #Check if user is in a channel
    if(voice_channel != None):
        if (vc is None):
            vc = await voice_channel.connect()
        #Interrupt the Bot if it is playing anything
        vc.stop()

        vc.play(discord.FFmpegPCMAudio(source), after=lambda e: print('done', e))

    else:
        await ctx.send("Join a voice channel first.")
    

def EmbedBlock(header, text):
        return discord.Embed(title=header, description=text, color=0xeb3434)

async def BuildHymnText(ctx, soup):
    header = soup.title.string
    print(header)
    body = soup.p.strings
    text = ""
    for string in body:
        if(string == "\n"):
            if(text != ""):
                e = EmbedBlock(header, text)
                await ctx.send(embed=e)
                text=""
                header=""
        else: 
            text += string
    if(text != ""):
        e = EmbedBlock(header, text)
        await ctx.send(embed=e)
        #e = EmbedBlock(header, string)
        #await ctx.send(string)

def setup(client):
        client.add_cog(TLH(client))

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

