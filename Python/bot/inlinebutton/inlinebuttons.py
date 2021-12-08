from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 Noutbuk", callback_data="laptop"),
        InlineKeyboardButton(text="📱 Telefon", callback_data="phone")
    ],
    [
        InlineKeyboardButton(text="🎮 PS5", url="https://www.playstation.com/ru-ru/ps5/"),
        InlineKeyboardButton(text="⌚️ Soat", callback_data="watch"),
    ],
    [
        InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat="")
    ]
    ]
)

forward = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ulashish", switch_inline_query="Zo'r ekan")
        ]
    ]
)