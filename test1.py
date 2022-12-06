import time
import logging
from aiogram import bot, dispatcher, executor, types, Bot, Dispatcher

TOKEN = "5419943736:AAFgOLEaN7WJD3ws0EKYIidapca8GuVsNmc"
HELP_COMMAND= """
/help - список команд
/start - начать работу с ботом 
"""

bot = Bot(token=TOKEN)
dp=Dispatcher(bot=bot)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text="Добро пожаловать)")
    await message.delete()



@dp.message_handler()
async def echo(message: types.Message):
	if message.text.count(' ')>=1 :
		await message.answer(text=message.text.upper())



if __name__ == '__main__':
	executor.start_polling(dp)