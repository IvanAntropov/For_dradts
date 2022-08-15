from aiogram import executor
from barter import dp

async def bot_on(_):
    print('Bot is on...')

from commands import conversation, media, other, ttt 
from keyboard import buttons
    
conversation.register_handlers_conversation(dp)
media.register_handlers_media(dp)
buttons.register_handlers_buttons(dp)

other.register_handlers_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_on)
    
    
    