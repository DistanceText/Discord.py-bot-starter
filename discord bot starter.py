import discord
from discord.ext import commands
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions
from apikeys import token
import datetime
from typing import List
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
clientprefix = '^'
BotRpc = "RPC"
startuptime = datetime.datetime.utcnow()
client = commands.Bot(command_prefix=clientprefix, intents=intents,status=discord.Status.idle)

@client.event
async def on_ready():
    print('Bot working as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=BotRpc),status=discord.Status.do_not_disturb)
    print('rpc set! at ', startuptime)
    print('Bot is now working! started at: ', startuptime)
    print('--------------------------------------------------------------')

@client.command()
async def hello(ctx):
    ctx.reply("Hi!")

client.run('YOUR TOKEN GOES HERE')
