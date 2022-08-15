from aiogram import types, Dispatcher
from barter import dp

async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')
        
def register_handlers_media(dp: Dispatcher):
    dp.register_message_handler(cats, commands = ['cat'])