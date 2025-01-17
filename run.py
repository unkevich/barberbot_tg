import asyncio
from aiogram import Bot, Dispatcher

from app.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Bot is Ready!")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is disabled!")