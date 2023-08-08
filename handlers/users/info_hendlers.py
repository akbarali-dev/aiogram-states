from aiogram import types
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink

from loader import dp
from states.personal_data import PersonalData


@dp.message_handler(commands='info_html')
async def bot_info(message: types.Message):
    text = f"Assalomu alekum, {message.from_user.full_name}!\n"
    text += "Bu -> <b>Qalin matn</b>\n"
    text += "Bu -> <i>Egri matn</i>\n"
    text += "Bu -> <u>Ostiga chizilgan matn</u>\n"
    text += "Bu -> <s>O'chirilgan matn</s>\n"
    text += "Bu -> <a href='https://mohirdev.uz'>Mohirdev sahifsiga link</a>\n"
    text += "Bu -> <code>print('Hello world!')</code>\n\n"

    await message.answer(text)


@dp.message_handler(commands='info_markdown')
async def bot_info(message: types.Message):
    text = f"Assalomu alekum, {message.from_user.full_name}\!\n"
    text += "Bu \-\> *Qalin matn*\n"
    text += "Bu \-\> _Egri matn_\n"
    text += "Bu \-\> __Ostiga chizilgan matn__\n"
    text += "Bu \-\> ~O'chirilgan matn~\n"
    text += "Bu \-\> [Mohirdev sahifsiga link](https://mohirdev.uz)\n"
    text += "Bu \-\> `print('Hello world!')`\n\n"

    await message.answer(text, parse_mode=types.ParseMode.MARKDOWN_V2)


@dp.message_handler(commands='info')
async def bot_info(message: types.Message):
    text = f"Assalomu alekum, {message.from_user.full_name}!\n"
    text += "Bu " + hbold("Qalin matn\n")
    text += "Bu " + hitalic("Egri matn\n")
    text += "Bu " + hunderline("Ostiga chizilgan matn\n")
    text += "Bu " + hstrikethrough("O'chirilgan matn\n")
    text += "Bu " + hlink("Mohirdev sahifsiga link\n", "https://mohirdev.uz ")
    text += "Bu " + hcode("print('Hello world!')\n\n")

    await message.answer(text)