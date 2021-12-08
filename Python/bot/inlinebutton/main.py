import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from inlinebuttons import menu, forward

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {user}😊", reply_markup=menu)


@dp.callback_query_handler()
async def callback(call):
    if call.message:
        if call.data == "laptop":
            msg = "<b>MacBook 13 Pro</b>\n<i>Narxi</i>: 1600 $\n<u>Chip</u>: M1"
            # await call.message.edit_text("Ulashishni hohlaysizmi", reply_markup=forward)
            await call.message.delete()
            await call.message.answer_photo("https://images.prismic.io/frameworkmarketplace/cca31de3-3b75-4932-af96-7646b7eba6c7__DSC3630-Edit-cropped.jpg?auto=compress,format", caption=msg, parse_mode="html", reply_markup=forward)
        elif call.data == "phone":
            msg = "<b>iPhone 13 Pro</b>\n<i>Narxi</i>: 1200 $\nKamera: 12MP"
            await call.message.answer_photo("https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F6148e5c7b85bfa189955ed22%2FApple-iPhone-13-Pro-Max-in-Sierra-Blue-%2F960x0.jpg%3Ffit%3Dscale", caption=msg, parse_mode="html")
            await call.message.delete()
        elif call.data == "watch":
            await call.message.answer("Qo'l soatini tanladingiz")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)