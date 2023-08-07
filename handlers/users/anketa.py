from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

from states.personal_data import PersonalData


@dp.message_handler(Command('anketa'))
async def enter_test(message: types.Message):
    await message.answer("to'lliq ismingizni kiriting")
    await PersonalData.full_name.set()


@dp.message_handler(state=PersonalData.full_name)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    # await state.update_data(name=fullname)
    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Email manzilingizni kiriting")
    await PersonalData.next()
    # await PersonalData.email.set()


@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text
    # await state.update_data(name=email)
    await state.update_data(
        {"email": email}
    )

    await message.answer("Telefon raqamingizni kiriting")
    await PersonalData.next()
    # await PersonalData.email.set()


@dp.message_handler(state=PersonalData.phone_number)
async def answer_email(message: types.Message, state: FSMContext):
    phone_num = message.text
    await state.update_data(
        {"phone": phone_num}
    )

    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    msg = "Quyidagi ma'lumotlar qabul qilindi\n"
    msg += f"Ismingiz: {name}\n"
    msg += f"Email: {email}\n"
    msg += f"Telefon: {phone}\n"

    await message.answer(msg)

    await state.finish()

