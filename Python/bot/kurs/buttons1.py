from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="EURO ➡️ UZS"),KeyboardButton(text="DOLLAR ➡️ UZS")],
        [KeyboardButton(text="RUBL ➡️ UZS"),KeyboardButton(text='TENGE ➡️ UZS')],
        [KeyboardButton(text="MIQDOR KIRITISH")]
    ],
    resize_keyboard=True,
    # one_time_keyboard=True
)