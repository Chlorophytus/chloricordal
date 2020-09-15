import chloricordal
import discord
from discord.ext import commands


@commands.command()
async def get_version(ctx: discord.ext.commands.Context):
    await ctx.send(f'I am Chloricordal v{chloricordal.__version__}')


def setup(bot: discord.ext.commands.Bot):
    bot.add_command(get_version)


def teardown(bot: discord.ext.commands.Bot):
    bot.remove_command(get_version)
