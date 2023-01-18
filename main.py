import discord
from dotenv import load_dotenv
from scraper import scrape
import os

load_dotenv()
my_token = os.getenv('TOKEN')
my_key = os.getenv('KEY')


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    while message.content.startswith('!'):
        if message.content.startswith('!scrape'):
            load = discord.Embed(title="Scraping...", description="Please wait while I scrape the marketplace for you", color=0x00ff00)
            load.set_image(url='https://cdn.dribbble.com/users/14275/screenshots/1882226/amc_loading.gif')
            await message.channel.send(embed=load)
            return await scrape(message)
        elif message.content.startswith('!help'):
            help = discord.Embed(title="Help", description='Format: !scrape item=:"ItemName" location="Location" distance="Distance"(No Spaces)\nAvailable Distance:1,2,5,10,20,40,60,65,80,100,250,500 \nExample: !scrape item=iPhone12 location=NewYork distance=50', color=0x00ff00)
            return await message.channel.send(embed=help)
        else:
            error = discord.Embed(title="Error", description="Invalid Command", color=0xff0000)
            return await message.channel.send(embed=error)


client.run(my_token)
