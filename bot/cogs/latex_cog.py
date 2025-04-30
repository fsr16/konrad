import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Cog, hybrid_command

from bot import utils


class LatexCommand(Cog):
    def __init__(self, bot):
        self.bot = bot

    @hybrid_command(name='latex', description='Gibt den angegeben Ausdruck als LaTeX-Ausdruck wieder')
    @app_commands.describe(ausdruck='Ausdruck, der in LaTeX angezeigt werden soll')
    async def latex(self, ctx: commands.Context[commands.Bot], ausdruck: str):
        result = utils.request_image(ausdruck)
        await ctx.send(file=discord.File(fp=result))

        utils.delete_file(result)
