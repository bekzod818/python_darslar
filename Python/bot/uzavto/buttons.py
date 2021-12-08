from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="💰 Avtomobil narxlari", callback_data="laptop")
    ],
    [
        InlineKeyboardButton(text="🚘 Avtomobillar informatsiyasi", callback_data="watch"),
    ],
    [
        InlineKeyboardButton(text="ℹ️ Sotuvda borligi to'g'risida", callback_data="info")
    ]
    ]
)