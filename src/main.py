import discord
from dotenv import load_dotenv
import os
import commands


# Getting token from .env
load_dotenv()
token = os.getenv("discord-token")

client = discord.Client()


@client.event
async def on_message(message):
    # From discord.py official documentation:
    # Since the on_message() event triggers for every message received,
    # we have to make sure that we ignore messages from ourselves.
    # We do this by checking if the Message.author is the same as the Client.user.
    if message.author == client.user:
        return

    # You can also use message.content.find("") == -1:
    if message.content.startswith("!hi"):
        await commands.hi(message)

    elif message.content.startswith("!time"):
        await commands.time(message)

    elif message.content.startswith("!help"):
        await commands.help_me(message)

    elif message.content.startswith("!game"):
        await commands.game(client, message)

client.run(token)
