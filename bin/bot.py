import discord
import sys
from discord.ext import commands
import chloricordal
import chloricordal.extensions
from chloricordal.checks import role
bot = commands.Bot(command_prefix='>')
modules = [
    'chat_logger',
    'dice',
    'hello',
    'get_version'
]


@bot.command()
async def ping(ctx: discord.ext.commands.Context):
    await ctx.send('Pong')


@bot.command()
@role.check_if(['Admin', 'Bot Control'])
async def graceful_quit(ctx: discord.ext.commands.Context):
    await ctx.send('Quitting gracefully')
    sys.exit(0)


@bot.group()
@role.check_if(['Admin', 'Bot Control'])
async def ext(ctx: discord.ext.commands.Context):
    if ctx.invoked_subcommand is None:
        await ctx.send('Please specify a subcommand: `insert | remove`.')


@ext.command()
async def insert(ctx: discord.ext.commands.Context, module: str):
    await ctx.send(f'Trying to **insert** module `{module}`')
    bot.load_extension('.'.join(['chloricordal', 'extensions', module]))


@ext.command()
async def remove(ctx: discord.ext.commands.Context, module: str):
    await ctx.send(f'Trying to **remove** module `{module}`')
    bot.unload_extension('.'.join(['chloricordal', 'extensions', module]))


@ext.command()
async def reload(ctx: discord.ext.commands.Context, module: str):
    await ctx.send(f'Trying to **reload** module `{module}`')
    bot.reload_extension('.'.join(['chloricordal', 'extensions', module]))

print("Running bootstrap:")
for module in modules:
    print(f"...{module}")
    bot.load_extension('.'.join(['chloricordal', 'extensions', module]))

print("*** success")
bot.run(sys.argv[1])
