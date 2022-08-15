from asyncore import dispatcher
from aiogram import types, Dispatcher
from barter import dp
from keyboard import kb1,kb2
from exercise import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from commands import other

async def send_welcome(message: types.Message):
    await message.answer("Привет, я - бот, который прикручен к дзшкам для прошлых семинаров. Вот какие комманды у меня есть:\n\
    /start - начальный экран с коммандами\n\
    /exMod - пока только дз с первого семинара\n\
    /other - что-нибудь прикручу, пока рассказывает анекдот.\n\
    /help - тоже самое что start\n\
    ", reply_markup=ReplyKeyboardRemove())
    
    
async def send_something(message: types.Message):
    await message.answer("Мужик купил три таблетки Виагры. Принес домой, на стол положил, пока переодевался — смотрит, а попугай их уже склевал… \n\
От злости схватил попугая и засунул в морозилку! Через полчаса отошёл от злости и решил выпустить попугая. \n\
Открывает морозилку, а там попугай весь в поту сидит. Мужик спрашивает:\n\
— Кеша, ты чего?\n\
Попугай:\n\
— А ты сам попробуй замороженной курице ноги раздвинуть…", reply_markup=kb2) # reply_makup=ReplyKeyboardRemove()
    
    
async def start_exMod(message: types.Message):
    await message.answer("Тут 5 заданий делают разные вещи, выбирай: ", reply_markup=kb1)
    
def register_handlers_conversation(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start','help'])
    dp.register_message_handler(send_something, commands=['other'])
    dp.register_message_handler(start_exMod, commands=['exMod'])
    dp.register_message_handler(send_welcome, commands=['exit'])
    dp.register_message_handler(start_ex1, commands=['ex1'])
    # dp.register_message_handler(ex2, commands=['ex2'])
    # dp.register_message_handler(ex3, commands=['ex3'])
    # dp.register_message_handler(ex4, commands=['ex4'])
    # dp.register_message_handler(ex5, commands=['ex5'])
    