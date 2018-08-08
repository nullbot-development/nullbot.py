import discord
from discord.ext import commands
import socket

bot = commands.Bot(command_prefix='$', description='NullBot is currently under development...')

# Terminal Display
@bot.event
async def on_ready():
    print('[+] SUCCESS!')
    print('[*] Logged in as: %s' % bot.user.name)

# Commands

class Basic:
    """Basic documentations"""

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Tests the bot's connectivity"""
        await bot.say("Pong!")
        print ("user has pinged")

bot.add_cog(Basic())


@bot.command(pass_context=True)
async def url(ctx, urlname):
    """'url [website]' - Determines IP address of URL."""
    urlnew = socket.gethostbyname(urlname)
    await bot.say('IP of %s: %s' % (urlname, urlnew))

@bot.command(pass_context=True)
async def purge(context, number : int):
    """'purge [number]' - Clear a specified number of messages in the chat"""
    deleted = await bot.purge_from(context.message.channel, limit=number)
    await bot.send_message(context.message.channel, 'Deleted {} message(s)!'.format(len(deleted)))

@bot.command(pass_context=True)
async def roles(context):
    """Displays all of the roles with their ids"""
    roles = context.message.server.roles
    result = "The roles are "
    for role in roles:
        result += role.name + ": " + role.id + ", "
    await bot.say(result)
    
