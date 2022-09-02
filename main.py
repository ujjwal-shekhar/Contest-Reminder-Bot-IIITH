import discord
from discord.ext import commands
import asyncio
import random
import os

## Check Scheduler

from datetime import datetime
day = datetime.now().day
half = os.getenv('HALF')

if half == '1' and day <= 15:
	print("Exiting")
	exit(0)
elif half == '0' and day > 15:
	print("Exiting")
	exit(0)

if day <= 15:
	print("Working in First Half")
else:
	print("Working in Second Half")


## Setup Client
intents = discord.Intents.all()
client = commands.Bot(command_prefix= 'cr;', intents = intents)



## Load Cogs
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension("cogs.{}".format(filename.replace('.py','').strip()))


##Testing 
@client.event
async def on_message(message):
	# Don't respond to ourselves
	if message.author == client.user:
		return

	# If bot is mentioned, reply with a message
	if client.user in message.mentions:
		await message.channel.send("Keyur too chad :)")
		return

## On Ready
@client.event
async def on_ready():
	print("Bot is Ready")
	channelTesting = client.get_channel(1014400159960027167)
	await channelTesting.send("Testing...")

	# channelPC = client.get_channel(712406461439017020)
	# await channelPC.send("The bot is ready now.")
	cnt = 0
	for g in client.guilds:
		cnt += len(g.members)
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{cnt} members !"))


## On Member Join
@client.event
async def on_member_join(member):
	print(f'{member} has joined our server!')



## On Member Remove
@client.event
async def on_member_remove(member):
	print(f'{member} has left our server!')


#Add Your Bot Token
token = os.getenv('CR_TOKEN',"NA")
if token == 'NA':
	token = os.environ['LOCAL_KEY']
	# token = ""

client.run(token)
