from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import course_callback, book_callback

category_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="Kitoblar", callback_data="books"),
        ],
        [
            InlineKeyboardButton(text="sahifaga o'tish",
                                 url="https://online.pdp.uz/course-play/deploying-to-cloud-computer"),
        ],
        [
            InlineKeyboardButton(text="qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="Ulashish", switch_inline_query="Zo'z bot ekan"),
        ]
    ]
)
# ======================================================================================================================
# 2-usul
courses_menu = InlineKeyboardMarkup(row_width=1)

python = InlineKeyboardButton(text="Python dasturlash asoslari", callback_data=course_callback.new(item_name="python"))
courses_menu.insert(python)

django = InlineKeyboardButton(text="Django dasturlash asoslari", callback_data=course_callback.new(item_name="django"))
courses_menu.insert(django)

telegram = InlineKeyboardButton(text="Telegram", callback_data="course:telegram")
courses_menu.insert(telegram)

aiogram = InlineKeyboardButton(text="Algorithm", callback_data="course:algorithm")
courses_menu.insert(aiogram)

back = InlineKeyboardButton(text="Orqaga", callback_data="cancel")
courses_menu.insert(back)
# ======================================================================================================================
# 3-isul

books = {
    "Python dasturlash asoslari": "python_book",
    "C++ dasturlash tili": "cpp_book",
    "Mukammal dasturlash. JavaScript": "js_book",
}

books_menu = InlineKeyboardMarkup(row_width=1)

for key, value in books.items():
    books_menu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))

books_menu.insert(back)
# ======================================================================================================================

telegram_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="xarid qilish", url="https://mohirdev.uz/courses/telegram/")
    ]
])

algorithm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ko'rish", url="https://mohirdev.uz/courses/algoritmlar/")
    ]
])
