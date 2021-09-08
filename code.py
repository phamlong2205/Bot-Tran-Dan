import discord
import random

TOKEN = 'ODg0OTY1OTE3NDA5MzEyNzY4.YTgKvA.EJz8U8HHjoSfiLKXenzZ-TdCwkE'

client = discord.Client()
sad_words = ["vl", "mẹ", "vcl", "đmm", "cc", "đm","lồn","ngu","cc","cặc","clm","clmmm","loz","chó","địt","đụ","dm","má"]

starter_encouragements = ["Mày chửi thề là tao lấy súng tao bắn mày đó"]

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
   username = str(message.author).split('#')[0]
   user_message = str(message.content)
   channel = str(message.channel.name)
   print(f'{username}: {user_message} ({channel})')

   if message.author == client.user:
   	return

   if any(word in user_message.lower() for word in sad_words):
   	await message.channel.send(f'Mày chửi thề là tao lấy súng tao bắn mày đó')

client.run(TOKEN)