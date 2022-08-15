from asyncore import dispatcher
from logging import exception
from aiogram import types, Dispatcher
from barter import dp
from keyboard import kb1,kb2
from exercise import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from commands import for_ex
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
    
urlkb = InlineKeyboardMarkup(row_width=2)
by = InlineKeyboardButton(text=f'yes',callback_data='yes')
bn = InlineKeyboardButton(text=f'no',callback_data='no')
urlkb.add(by,bn)


# class FSMAdmin(StatesGroup):
#     number = State()
#     choose = State()


async def start_ex1(message: types.Message):
    await message.answer("Программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.", reply_markup=kb2)
    # await FSMAdmin.number.set()
    await message.answer(f"Enter the number: ")
    dp.register_message_handler(ex1)
       
async def ex1(message: types.Message,callback: types.CallbackQuery):
    try:
        number = int(message.text)
        if number > 7 or number < 1:
            await message.answer("Try again. You must enter the number of the day.")
            ex1
        else:
            if number == 6 or number == 7:
                await message.answer(f'{number} -> weekend')
                await message.answer("Again?",reply_markup=urlkb)
                # dp.register_message_handler(choose)
            else:
                await message.answer(f'{number} -> weekdays')
                await message.answer("Again?",reply_markup=urlkb)
                ch = callback.text
                if ch == 'yes':
                    dp.register_message_handler(start_ex1)
                if ch == 'no':
                    dp.register_message_handler(for_ex.start_exMod)
                    # dp.register_message_handler(choose)
    except ValueError:
        await message.answer("Try again. You must enter the number of the day.")

async def choose(callback: types.CallbackQuery):
    ch = callback.text
    if ch == 'yes':
        dp.register_message_handler(start_ex1)
    if ch == 'no':
        dp.register_message_handler(for_ex.start_exMod)
        
        
            
