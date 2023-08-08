from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.menu_keyboards import menu
from keyboards.default.python_keyboards import menu_python
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("kursni tanlang", reply_markup=menu)


@dp.message_handler(Text("Boshiga"))
async def main(message: Message):
    await message.answer("kursni tanlang", reply_markup=menu)


@dp.message_handler(Text('telegram bot'))
async def telegram_bot(message: Message):
    await message.answer("Telegram bot kursi", reply_markup=menu)


@dp.message_handler(Text('Python'))
async def python_menu(message: Message):
    await message.answer("Mavzu tanlang", reply_markup=menu_python)


@dp.message_handler(Text('#00 kirish'))
async def first_lesson(message: Message):
    await message.answer("Kirish qismiga xush kelibsiz", reply_markup=ReplyKeyboardRemove())
