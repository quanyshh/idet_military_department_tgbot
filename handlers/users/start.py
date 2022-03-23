from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
import logging

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    logging.info(f"id={message.from_user.id}, full_name={message.from_user.full_name}, locale={message.from_user.locale}, mention={message.from_user.mention},  username={message.from_user.username}")

   
    await message.answer(f"Привет, {message.from_user.full_name}! Нажми /menu")
