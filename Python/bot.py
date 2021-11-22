import logging

import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from contextlib import suppress

from aiogram import types
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
    MessageToDeleteNotFound)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
API_TOKEN = "1814756712:AAGEqkxTPIquhWeh9_WWdI84AoeWaKUqlxM"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# keyboards
inline_btn_1 = InlineKeyboardButton('Delete this message', callback_data='del1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot with delete messages!\nPowered by aiogram.",
        reply_markup=inline_kb1)

@dp.message_handler()
async def echo(message: types.Message):
    msg = await message.reply(message.text, reply_markup=inline_kb1)

# @dp.callback_query_handler(func=lambda c: c.data == 'del1')
@dp.callback_query_handler()
async def process_callback_del1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Message deleted!")
    msg = callback_query.message
    rmsg = callback_query.message.reply_to_message
    asyncio.create_task(delete_message(rmsg, 1))
    asyncio.create_task(delete_message(msg, 1))
    # asyncio.create_task(delete_message(rmsg, 5))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


