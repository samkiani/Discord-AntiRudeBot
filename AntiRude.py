import discord
import json
from persiantools.jdatetime import JalaliDateTime
from random import choice

class CONFIG:
        TOKEN = '' #str
        GUILD_ID = 0 #int
        CHANNEL_ID = 0 #int

client = discord.Client(Intents = discord.Intents.all())



sokhan = ['Bi adab' , 'Bi adabo bebina' , 'Khejalat nakesh' , 'Bi farhang' , 'Effate kalamet ku?' , 'Tasbih bezan' ,
          'Adab nadari mage?' , 'Bi nezakat' , 'Cheghad bi adab' , 'Chenghade bi adab' , 'So bi adab' , 'Bishour']


with open('AntiRudeBot/BadWords.json' , encoding = 'utf-8') as bw:
        datalist = []
        data = json.load(bw)
        for badwords in data['words']:
                datalist.append(badwords)


@client.event
async def on_error():
        pass


@client.event
async def on_ready():
        guild = client.get_guild(CONFIG.GUILD_ID)
        channel = guild.get_channel(CONFIG.CHANNEL_ID)
        await channel.connect()
        await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching , name = 'Rude Members ►►► Developed by ErfanNJZ'))
        print(JalaliDateTime.today() ,'\n\nBot Online Shod XD\nDeveloped by ErfanNJZ')


@client.event
async def on_message(message):
    for word in datalist:
        if word in message.content:
                await message.delete()
                await message.channel.send(f'>>> {message.author.mention}  {choice(sokhan)}')



client.run(CONFIG.TOKEN)