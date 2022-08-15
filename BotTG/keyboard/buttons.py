from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup
from aiogram import types, Dispatcher
from barter import dp, bot


inline_btn_1 = InlineKeyboardButton('кнопка', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
kb = ReplyKeyboardMarkup()

async def process_command_1(message: types.Message):
    await message.reply("кнопище", reply_markup=inline_kb1)
    
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'кнопка!')
    
def register_handlers_buttons(dp: Dispatcher,callback : types.CallbackQuery):
    dp.register_message_handler(process_command_1, commands=['1'],)
    dp.register_message_handler(process_callback_button1, callback_data == 'button1')
    
