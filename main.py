


import logging
import wikipedia



from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5604462170:AAENgrkt9N18hikCNj3sv7rVg65bVMu0nUc'
wikipedia.set_lang('uz')


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
    await message.reply("Salom Wikipedia botga xush kelibsiz.Wikipediadan malumot izlash uchun matn kiriting. Bu bot Babur Sarsenbaev tomonidan yaratildi"
                        "Bizni telegramda kuzatish .Business_IT_1")



@dp.message_handler()
async def sendWiki(message: types.Message):
      try:
          respond = wikipedia.summary(message.text)
          await message.answer(respond)

      except:
          await message.answer("Bu mavzuga oid malomut topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
