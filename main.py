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
            return await scrape(message)
        elif message.content.startswith('!help'):
            return await message.channel.send(
                'Format: !scrape item="Item name" location="Location" distance="Distance"(No Spaces)\nAvailable Distance:1,2,5,10,20,40,60,65,80,100,250,500 \nExample: !scrape item=iPhone 12 location=New York distance=50')
        else:
            return await message.channel.send('Unknown command')


client.run(my_token)
