import discord
from discord.ext import commands
from discord.utils import find
from typing import List


def check_if(the_roles: [str]):
    """
    A command check decorator that checks for a Discord role.

    :param the_roles: The roles to check for.
    """
    async def predicate(ctx: discord.ext.commands.Context):
        author: discord.Member = ctx.author
        roles: List[discord.Role] = author.roles
        return discord.utils.find(lambda role: any(role.name == that for that in the_roles), roles) \
            is not None
    return commands.check(predicate)
