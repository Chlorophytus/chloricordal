import discord
from discord.ext import commands


@commands.command()
async def hello(ctx: discord.ext.commands.Context):
    await ctx.send(f'Hello {ctx.author.display_name}')


def setup(bot: discord.ext.commands.Bot):
    bot.add_command(hello)


def teardown(bot: discord.ext.commands.Bot):
    bot.remove_command(hello)
