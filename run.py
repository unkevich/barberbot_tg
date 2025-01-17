import asyncio
from aiogram import Bot, Dispatcher

from app.config import TOKEN
from app.handlers import router

async def main():
    try:
        bot = Bot(token=TOKEN)
        dp = Dispatcher()

        dp.include_router(router=router)
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Error | {e}")

if __name__ == "__main__":
    try:
        print("Bot is Ready!")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is disabled!")