from bot import Bot
import asyncio

async def main():
    bot = Bot()
    await bot.start()
    await asyncio.Event().wait()  # Keeps the bot running

if __name__ == "__main__":
    asyncio.run(main())
