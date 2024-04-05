from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from asyncio import run

import wikipedia


wikipedia.set_lang("uz")

API_TOKEN = '6867964702:AAFwaB0qm9DmE5IkGt6IWRSVPwJ-xkL9nJk'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_cmd(message:Message):
   await message.reply(f'Assalamu alaykum wikipedia botga xush kelibsiz.'
                       '\n \n'
                       'Siz bu yerdan o`zingiz hohlagan ma`lumotlarni topishingiz mumkun')

async def main():
   await bot.delete_webhook(drop_pending_updates=True)
   await dp.start_polling(bot)

@dp.message()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi!")

if __name__ == '__main__':
    run(main())