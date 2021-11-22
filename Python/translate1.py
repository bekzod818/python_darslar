from googletrans import Translator
from googletrans import LANGUAGES

# print(LANGUAGES.keys())

matn_lang = input("Siz qaysi tilda kiritmoqchisiz: ")
matn = input("Tarjima qilmoqchi bo'lgan matnni kiriting: ")
lang = input("Siz qaysi tilga tarjima qilmoqchisiz: ")
tarjimon = Translator()
tarjima = tarjimon.translate(matn, src=matn_lang, dest=lang)
print("_*" * 10)
print(tarjima.text)