import discord
from discord import app_commands
from discord.ext.commands import Cog, command

from bot import utils
#from bot.konrad import Konrad


class LatexCommand(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name='latex', description='Gibt den angegeben Ausdruck als LaTeX-Ausdruck wieder')
    @app_commands.describe(ausdruck='Ausdruck, der in LaTeX angezeigt werden soll')
    async def latex(self, interaction, ausdruck: str):
        result = utils.request_image(ausdruck)
        await interaction.response.send_message(file=discord.File(fp=result))

        utils.delete_file(result)
