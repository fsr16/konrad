from discord import Intents
from discord.ext.commands import Bot

from bot.cogs.gray_room_cog import GrayRoomCog
from bot.cogs.latex_cog import LatexCommand
from bot.cogs.message_cog import MessageEventsCog

bot_modules = [
    MessageEventsCog,
    GrayRoomCog,
    LatexCommand,
]


class Konrad(Bot):
    def __init__(self):
        super().__init__(command_prefix=None, intents=Intents.all())

    async def setup_hook(self):
        for module in bot_modules:
            await self.add_cog(module(self))
        print("Cogs loaded")

    async def on_ready(self):
        print(f"Bot is online as '{self.user}'")
        await self.tree.sync()
        print("Synced slash commands.")
