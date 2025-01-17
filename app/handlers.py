from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    try:
        await message.answer(text="*Привет, это официальный бот нашего барбершопа! ✂️*\n*Здесь ты можешь:*\n*– Записаться на стрижку или бритьё. 🕖*\n*– Узнать о наших услугах и ценах. 💈*\n*– Посмотреть акции и специальные предложения. 💥*\n\n*Чтобы начать, выбери нужный пункт в меню или введи команду.*", reply_markup=kb.menu, parse_mode="MarkDown")
    except Exception as e:
        print(f"Error | {e}")