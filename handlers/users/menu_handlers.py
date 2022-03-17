from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.menu_keyboards import language_keyboard, main_menu_keyboard, questions_keyboard, question_keyboard, menu_cd
from loader import dp
from utils.db_api.database import data


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await list_of_languages(message)

async def list_of_languages(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await language_keyboard()

    if isinstance(message, types.Message):
        await message.answer("Выберите язык!", reply_markup=markup)
    
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)

async def list_main_menu(callback: types.CallbackQuery, language, **kwargs):
    markup = await main_menu_keyboard(language)

    await callback.message.edit_reply_markup(markup)

async def list_questions(callback: types.CallbackQuery, language, main_menu, **kwargs):
    markup = await questions_keyboard(language = language, main_menu = main_menu)

    await callback.message.edit_text("Военная подготовка на военной кафедре Satbayev University", reply_markup=markup)

async def show_question(callback: types.CallbackQuery, language, main_menu, questions, question_id):
    markup = question_keyboard(language, main_menu, questions, question_id)
    text = f"{data[questions]}"
    id = int(questions[-1])
    # if id == 8:
    #     await callback.message.send_photo(photo=open('btn8_kaz.png', 'rb'))
    # else:
    await callback.message.edit_text(text, reply_markup=markup, parse_mode="HTML")


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    language = callback_data.get('language')
    main_menu = callback_data.get('main_menu')
    questions = callback_data.get('questions')
    question_id = callback_data.get('question_id')


    levels = {
        "0": list_of_languages,
        "1": list_main_menu,
        "2": list_questions,
        "3": show_question
    }

    current_level_function = levels[current_level]

    await current_level_function(
        call,
        language = language,
        main_menu = main_menu,
        questions=questions,
        question_id = question_id
    )