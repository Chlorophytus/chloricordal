import discord
import sys
from discord.ext import commands
from checks import role
bot = commands.Bot(command_prefix='>')


@bot.command()
async def ping(ctx: discord.ext.commands.Context):
    await ctx.send('pong')

@bot.command()
@role.check_if('Bot Admin')
async def graceful_quit(ctx: discord.ext.commands.Context):
    await ctx.send('Quitting gracefully')
    sys.exit(0)


bot.load_extension('hello')
bot.run(sys.argv[1])
