import discord
import logging
import logging.handlers
import os


logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    file_handler = logging.handlers.TimedRotatingFileHandler(
        os.path.join("log", "chloricordal.log"))
    format = logging.Formatter(
        '<%(name)s> (%(levelname)s)\t%(message)s')
    handler.setFormatter(format)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.addHandler(file_handler)


async def on_message(message: discord.Message):
    logger.log(
        logging.INFO, f"{message.created_at.isoformat(timespec='milliseconds')} ({message.jump_url}) <{message.author.name}#{message.author.discriminator} #{message.channel.name}>: {message.content}")


def setup(bot: discord.ext.commands.Bot):
    bot.add_listener(on_message)


def teardown(bot: discord.ext.commands.Bot):
    bot.remove_listener(on_message)
