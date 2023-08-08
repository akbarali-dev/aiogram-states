import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from keyboards.default.menu_keyboards import menu
from keyboards.inline.products_keyboard import category_menu, courses_menu, books_menu, telegram_keyboard
from keyboards.inline.callback_data import book_callback, course_callback
from loader import dp


@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(message: Message):
    await message.answer("Mahsulotlar tanlang", reply_markup=category_menu)


@dp.callback_query_handler(text="courses")
async def show_menu(call: CallbackQuery):
    await call.message.answer("Kurs tanlang", reply_markup=courses_menu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="books")
async def buy_books(call: CallbackQuery):
    await call.message.answer("kitoblar", reply_markup=books_menu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(course_callback.filter(item_name="telegram"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.message.answer("Siz mukammal telegram bot kursini tanadingiz", reply_markup=telegram_keyboard)
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="python_book"))
async def buying_course(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)


@dp.callback_query_handler(text="cancel")
async def buy_books(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=category_menu)
    await call.answer()