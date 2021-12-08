import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = '2106640014:AAFPE196Nb4JI4afWXw7VKuKm6D_s5UbqRY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
@dp.message_handler()
async def echo(message: types.Message):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{message.text}/").json()
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer(response[0]['phonetics'][0]['audio'])
    await message.answer_voice(response[0]['phonetics'][0]['audio'][2:])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)