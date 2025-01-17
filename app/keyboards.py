from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Личный кабинет"), KeyboardButton(text="Запись на услуги")],
    [KeyboardButton(text="Услуги и цены"), KeyboardButton(text="Акции и скидки")],
    [KeyboardButton(text="Отзывы")]
], resize_keyboard=True, input_field_placeholder="Выберите пункт меню...")