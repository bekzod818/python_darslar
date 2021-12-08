from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Foydalanuvchilar")],
        [KeyboardButton(text="Bog'lanish"), KeyboardButton(text="Obuna bo'lish")],
        [KeyboardButton(text="Qo'shimcha fikrlar"), KeyboardButton(text="Rasmlar")]
    ],
    resize_keyboard=True,
    # one_time_keyboard=True
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Telefon raqam", request_contact=True), KeyboardButton(text="📍 Joylashuv", request_location=True)],
        [KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True,
)