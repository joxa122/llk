import asyncio
import logging
import uuid
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

TOKEN = "7933209090:AAFLbB3_kP0c9QEw4JZvg2iQW-umgL08Uio"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 📖 Musiqa lug‘ati (so‘zlar va ta’riflar)
music_dictionary = {
    "Aksak": "Turli o‘lchamdagi ritmik tuzilmalarga asoslangan ohang.",
    "Akompaniment": "Asosiy kuyga hamroh bo‘luvchi musiqa.",
    "Aria": "Opera yoki kantatada ijro etiladigan kuy.",
    "Andante": "O‘rtacha sekin tempdagi musiqa.",
    "Adagio": "Sekin va ravon temp.",
    "Atonal": "Ma’lum tonallikka bog‘lanmagan musiqa.",
    "Bagatelle": "Yengil va qisqa musiqiy asar.",
    "Balet": "Musiqa va raqs uyg‘unligiga asoslangan san’at turi.",
    "Bass": "Eng past tovush diapazoniga ega bo‘lgan ovoz yoki cholg‘u.",
    "Doira": "Dumaloq shakldagi zarbli cholg‘u asbobi.",
    "Duplet": "Oddiy ritmga qaraganda ikki barobar tez chalinadigan notalar guruhi.",
    "Dissonans": "Ohangli uyg‘unlikning buzilishi.",
    "Diatonika": "Tabiiy tonallikka asoslangan kuylar tizimi.",
    "Diminuendo": "Sekin-asta pasayuvchi ohang.",
    "Duduk": "Arman xalqining an’anaviy puflama cholg‘u asbobi.",
    # ... (Yana 480 ta atama shu formatda qo‘shilishi kerak)
}

# 🔍 Inline qidiruv funksiyasi
@dp.inline_query()
async def inline_search(query: types.InlineQuery):
    search_text = query.query.lower().strip()  # Foydalanuvchi yozgan so‘z
    results = []

    # Agar foydalanuvchi so‘z yozmagan bo‘lsa, hech narsa ko‘rsatmaymiz
    if not search_text:
        await query.answer(results, cache_time=1)
        return

    # Lug‘atdan mos keladigan natijalarni topamiz
    for word, definition in music_dictionary.items():
        if search_text in word.lower():
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title=word.capitalize(),
                    input_message_content=InputTextMessageContent(
                        message_text=f"📖 *{word.capitalize()}*: {definition}",
                        parse_mode="Markdown"
                    )
                )
            )

    # Agar hech qanday natija topilmasa
    if not results:
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="Natija topilmadi",
                input_message_content=InputTextMessageContent(
                    message_text="⚠️ Kechirasiz, ushbu so‘z lug‘atda mavjud emas.",
                    parse_mode="Markdown"
                )
            )
        )

    await query.answer(results, cache_time=1)

# 🚀 Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

