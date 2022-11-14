
import discord

import bot

from discord.ext import commands, tasks
import os

import random
# import PyNaCl
from discord.ext import commands
import string
import random

TOKEN = 'MTA0MTQyMTg0NzQ1NzE2OTQwOA.GZldHG.RxwWBsiomhgNdRZYX5Ss-G9amN2_YU_Trp4qDY'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='!', intents=intents)


# Conversation Code
# bot.add_command(test12)
@client.event
async def on_ready():
    print('Hello. You have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):

    if message.author == client.user:
        return
    else:
       await bot.command(message)




client.run(TOKEN)
