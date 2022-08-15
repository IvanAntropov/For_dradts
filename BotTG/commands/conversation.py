from asyncore import dispatcher
from aiogram import types, Dispatcher
from barter import dp
from keyboard import kb_user
from aiogram.types import ReplyKeyboardRemove

async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm GAY!!!", reply_markup=kb_user)
    
async def send_something(message: types.Message):
    await message.reply("Hi!\nYou're GAY!!!") # reply_makup=ReplyKeyboardRemove()
    
def register_handlers_conversation(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start','help'])
    dp.register_message_handler(send_something, commands=['who'])
    