from aiogram import *
import time

TOKEN = "5957898759:AAFm_eGpDeAHSGiIxFwqom7ECY0wgw3hk3Y"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def start(message: types.message):
    user_name = message.from_user.full_name
    chat_id = message.from_user.id
    await bot.send_message(chat_id, "Привет, "+user_name+"!\nЯ тестовый бот Python разработчика SoulRedemption!\nНадеюсь, тебе понравится мой функционал❤️")

@dp.message_handler(content_types=['text'])
async def horosho(message):
    if "хорошо" in message.text.lower():
        message_bot = await message.reply('Хорошо')
        time.sleep(60)
        await message_bot.delete()
if __name__ == "__main__":
    executor.start_polling(dp)
    