import asyncio

import discord

import requests
from aiohttp import request
from discord.ext import commands, tasks
import os
import youtube_dl
import random
# import PyNaCl
from discord.ext import commands

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
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    print(user_message)
    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

    if user_message.lower().startswith('hello') or user_message.lower().startswith('hi'):
        await message.channel.send(f'Hello {username}')
        return
    elif user_message.lower() == "bye":
        await message.channel.send(f'Bye {username}')
    elif user_message.lower() == "tell me a joke":
        jokes = [" Can someone please shed more\
            light on how my lamp got stolen?",
                 "Why is she called llene? She stands on equal legs.",
                 "What do you call a gazelle in a \
                     lions territory? Denzel."]
        await message.channel.send(random.choice(jokes))


client.run(TOKEN)