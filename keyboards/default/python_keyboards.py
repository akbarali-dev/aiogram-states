from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_python = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='#00 kirish'),
            KeyboardButton(text='#01 kerakli dasturlar'),
            KeyboardButton(text='#02 Hello world'),
        ],
[
            KeyboardButton(text='Ortga'),
            KeyboardButton(text='Boshiga'),
        ]
    ],
    resize_keyboard=True
)