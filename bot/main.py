import asyncio
import os

from dotenv import load_dotenv

from bot.konrad import Konrad

load_dotenv()


async def main():
    await Konrad().start(os.getenv('TOKEN'))


if __name__ == "__main__":
    asyncio.run(main())
