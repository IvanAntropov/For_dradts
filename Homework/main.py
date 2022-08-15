from aiogram import executor
from barter import dp

async def bot_on(_):
    print('Bot is on...')

from commands import for_ex, other
    
for_ex.register_handlers_conversation(dp)

# other.register_handlers_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_on)