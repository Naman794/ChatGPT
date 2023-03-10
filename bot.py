import discord
import threading, json
import asyncio
import logging, os
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown, when_mentioned_or, MissingRequiredArgument
from discord.ext import commands
import random, asyncio, json, time
from datetime import datetime
from time import sleep
import secrets
import sqlite3
import logging
from discord.utils import get

msg_id = None
bot = commands.Bot(command_prefix=commands.when_mentioned_or("r!"),
                   intents=discord.Intents.all())
                   
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print("Owner Name: 𝐀𝐌𝐀𝐙𝐈𝐍𝐆 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄#6700")
    print("Owner ID: 485489178583498764")


@bot.event
async def on_connect():
    # Settings 'Listening' status
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="45,723 users data stored!"))
         

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='bot.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



async def load_extensions():
    for filename in os.listdir("./src"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")
                
async def main():
    async with bot:
        await load_extensions()
        await bot.start('TOKEN')

asyncio.run(main())
