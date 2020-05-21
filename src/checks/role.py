import discord
from discord.ext import commands
from discord.utils import find
from typing import List


def check_if(the_role: str):
    """
    A command check decorator that checks for a Discord role.

    :param the_role: The role to check for.
    """
    async def predicate(ctx: discord.ext.commands.Context):
        author: discord.Member = ctx.author
        roles: List[discord.Role] = author.roles
        return discord.utils.find(lambda role: role.name == the_role, roles) \
            is not None
    return commands.check(predicate)
