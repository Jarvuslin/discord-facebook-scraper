import discord


from scraper import scrape

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

    if message.content.startswith('!scrape'):
        return await scrape(message)


client.run('MTA2MzY2MzEyMjA1NDkyMjI2MQ.GQ6Msz.FJry9I4AxHVUmAFWx6nEHdoEZEq4bKaMdNRoqQ')