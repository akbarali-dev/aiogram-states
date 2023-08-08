from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Mahsulotlar'),
            KeyboardButton(text="Qo'llanma")
        ]
    ],
    resize_keyboard=True
)



# menu_start = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='Contact', request_contact=True),
#             KeyboardButton(text='Location', request_location=True)
#         ]
#     ],
#     resize_keyboard=True
# )
