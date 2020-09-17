import discord
from discord.ext import commands
from num2words import num2words
import random
import re

DICE_ROLL_RE: re.Pattern = re.compile(r"([0-9]+)d([0-9]+)")


def check_sanity_prefix(prefix: int):
    return prefix > 0 and prefix < 9


def check_sanity_suffix(suffix: int):
    return suffix > 1 and suffix < 2049


@commands.command()
async def roll(ctx: discord.ext.commands.Context, *, dice_string: str):
    results: [str] = []
    await ctx.send(f":game_die: Attempting to roll...")
    for di, df in enumerate(re.finditer(DICE_ROLL_RE, dice_string), start=1):
        prefix = int(df[1])
        suffix = int(df[2])
        if di > 24:
            break
        ordinal = num2words(di, to='ordinal')
        if check_sanity_prefix(prefix) and check_sanity_suffix(suffix):
            dice_result: [int] = []
            for _ in range(prefix):
                dice_result.append(random.randint(1, suffix))
            result = ', '.join([str(what) for what in dice_result])
            results.append(f"- The {ordinal} roll resulted in: **{result}**\n")
    done = ''.join(results)
    await ctx.send(f""":game_die: Results:
```markdown
{done}```""")


def setup(bot: discord.ext.commands.Bot):
    bot.add_command(roll)


def teardown(bot: discord.ext.commands.Bot):
    bot.remove_command(roll)
