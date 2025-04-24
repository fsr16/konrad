import discord
from discord import app_commands
import os

from dotenv import load_dotenv

import botactions
import gr
import latex

load_dotenv()


def init():
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)

    botactions.init(client, tree)
    gr.init(client, tree)
    latex.init(client, tree)

    client.run(os.getenv('TOKEN'))
