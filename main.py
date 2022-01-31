#Copyright Devin B (Azura4k) 2022, All Rights Reserved

#Imports
import discord
import logging
from decouple import config
from common.moderation import Moderation

#Configs
APPID = config('APPID')
TOKEN = config('TOKEN')
PublicKey = config('PUBLICKEY')
client = discord.Client()
logging.basicConfig(level=logging.INFO)
#Assignment
Mod = Moderation(0.8)

@client.event
async def on_message(message):
    if Mod.SafeMsgWordScanner(message.content) == False:
        #Check for administrator level override
        #if not message.author.guild_permissions().administrator():
        await message.delete()
        Sendback = f"{message.author.mention} Prohibited Word Used"
        await message.channel.send(Sendback)

    elif Mod.SafeMsgSequenceScanner(message.content) == False:
        await message.delete()
        Sendback = f"{message.author.mention} Prohibited Word Detected In Sequence"
        await message.channel.send(Sendback)
    #Command Checks
    if message.content.startswith('!akatsuki'):
        await message.channel.send("Hello, I'm Akatuski. Owned and Created by Azura4k.")

PermissionInt = int(8)

client.run(TOKEN)