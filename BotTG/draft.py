from gc import callbacks
import logging
from aiogram import Bot, Dispatcher
from asyncore import dispatcher
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram import executor

logging.basicConfig(level=logging.INFO)

async def bot_on(_):
    print('Bot is on...')

API_TOKEN = 'token'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
 
ID = user.id
   
grid = [' ',' ',' ',' ',' ',' ',' ',' ',' '] 
xo =['x','o']
urlkb = InlineKeyboardMarkup(row_width=2)
button_game_again = InlineKeyboardButton(text = 'Еще раз', callback_data = 'www')
button_exit = InlineKeyboardButton(text='Выйти', url = 'https://youtube.com')
b1 = InlineKeyboardButton(text=f'{grid[0]}',callback_data='0')
b2 = InlineKeyboardButton(text=f'{grid[1]}',callback_data='1')
b3 = InlineKeyboardButton(text=f'{grid[2]}',callback_data='2')
b4 = InlineKeyboardButton(text=f'{grid[3]}',callback_data='3')
b5 = InlineKeyboardButton(text=f'{grid[4]}',callback_data='4')
b6 = InlineKeyboardButton(text=f'{grid[5]}',callback_data='5')
b7 = InlineKeyboardButton(text=f'{grid[6]}',callback_data='6')
b8 = InlineKeyboardButton(text=f'{grid[7]}',callback_data='7')
b9 = InlineKeyboardButton(text=f'{grid[8]}',callback_data='8')



@dp.message_handler(commands='1')
async def buttons(message : types.Message):
    await message.answer('Тадам', reply_markup=urlkb)
    
@dp.callback_query_handler(text=['0','1'])
async def but1(callback : types.CallbackQuery):
    grid[callback_data] = xo[user]
    b1 = InlineKeyboardButton(text=f'{grid[0]}',callback_data='0')
    await callback.message.answer(f'{text}')
    await callback.answer()
    
urlkb.row(b1,b2,b3).row(b4,b5,b6).row(b7,b8,b9).add(button_game_again,button_exit)
    
    
    

    
    
    
    
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_on)
    
# button_hi = KeyboardButton('Привет! 👋')

# greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет!", reply_markup=greet_kb1)
    
# inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
# inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# #bot.py
# @dp.message_handler(commands=['Привет! 👋'])
# async def process_command_1(message: types.Message):
#     await message.reply("Первая инлайн кнопка", reply_markup=inline_kb1)
    
# @dp.callback_query_handler(func=lambda c: c.data == 'button1')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')



# from aiogram.types import ReplyKeyboardRemove, \
#     ReplyKeyboardMarkup, KeyboardButton, \
#     InlineKeyboardMarkup, InlineKeyboardButton


# button_hi = KeyboardButton('Привет! 👋')

# greet_kb = ReplyKeyboardMarkup()
# greet_kb.add(button_hi)

# greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

# greet_kb2 = ReplyKeyboardMarkup(
#     resize_keyboard=True, one_time_keyboard=True
# ).add(button_hi)

# button1 = KeyboardButton('1️⃣')
# button2 = KeyboardButton('2️⃣')
# button3 = KeyboardButton('3️⃣')

# markup3 = ReplyKeyboardMarkup().add(
#     button1).add(button2).add(button3)

# markup4 = ReplyKeyboardMarkup().row(
#     button1, button2, button3
# )

# markup5 = ReplyKeyboardMarkup().row(
#     button1, button2, button3
# ).add(KeyboardButton('Средний ряд'))

# button4 = KeyboardButton('4️⃣')
# button5 = KeyboardButton('5️⃣')
# button6 = KeyboardButton('6️⃣')
# markup5.row(button4, button5)
# markup5.insert(button6)

# markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
#     KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
# ).add(
#     KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
# )

# markup_big = ReplyKeyboardMarkup()

# markup_big.add(
#     button1, button2, button3, button4, button5, button6
# )
# markup_big.row(
#     button1, button2, button3, button4, button5, button6
# )

# markup_big.row(button4, button2)
# markup_big.add(button3, button2)
# markup_big.insert(button1)
# markup_big.insert(button6)
# markup_big.insert(KeyboardButton('9️⃣'))


# async def test(message: types.Message):
#     await message.reply("Привет!")

# inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
# inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# inline_kb_full = InlineKeyboardMarkup(row_width=2, column_width=2).add(inline_btn_1)
# inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))
# inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
# inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
# inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
# inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
# inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
# inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
# inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
# inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
# inline_kb_full.add(InlineKeyboardButton('Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))


    
# @dp.message_handler(commands=['s1'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет!", reply_markup=greet_kb)
    
# @dp.message_handler(commands=['s2'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет!", reply_markup=inline_kb_full)
    
# @dp.message_handler(commands=['s3'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет!", reply_markup=markup5)
    

    
    
    
    
    
    
    
    
    
    



    






# from commands import *
# from aiogram import Bot, Dispatcher, executor, types


# logging.basicConfig(level=logging.INFO)


# Dispatcher(Bot('5535805074:AAH9hPsG9EsJQXRQGCT3fI4F1KaxgKAsMjQ')).message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    
# @dp.message_handler(commands=['startXO'])
# async def theGame(message: types.Message):
#     listOfXO = [' ', 'x', 'o']
#     grid = ['          \n     ',' | ',' | ',' \n  -----------  \n   ',' | ',' | ',' \n  -----------  \n   ',' | ',' | ',' \n          ']
#     count = 0
#     listOfPosition = [0,0,0,0,0,0,0,0,0]
#     forWin = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]] 
#     playersList = [[],[]]
#     await message.answer('\nИгроки по очереди ставят на свободные клетки крестики и нолики.\nПервый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.')
#     await message.answer(grid[0] + 
#         '1' + grid[1] + '2' + grid[2] + '3' + grid[3] + 
#         '4' + grid[4] + '5' + grid[5] + '6' + grid[6] + 
#         '7' + grid[7] + '8' + grid[8] + '9' + grid[9])
#     turn = random.randint(1, 2)
#     await message.answer(f'Первый ход за {listOfXO[turn]}.\n')
#     while count != 9:
#         await message.answer(grid[0] + 
#         listOfXO[listOfPosition[0]] + grid[1] + listOfXO[listOfPosition[1]] + grid[2] + listOfXO[listOfPosition[2]] + 
#         grid[3] + 
#         listOfXO[listOfPosition[3]] + grid[4] + listOfXO[listOfPosition[4]] + grid[5] + listOfXO[listOfPosition[5]] + 
#         grid[6] + 
#         listOfXO[listOfPosition[6]] + grid[7] + listOfXO[listOfPosition[7]] + grid[8] + listOfXO[listOfPosition[8]] + 
#         grid[9])
#         check = False
#         while not check:
#             await message.answer(f'Ход игрока {listOfXO[turn]}\nВыбери квадрант 1 - 9: ')
#             check = False
#             while not check:
#                 try:
#                     number = int(message.text)
#                     pause
#                     if number >= 1 and number <= 9:
#                         player = number
#                         check = True
#                     else:
#                         await message.answer(f'Ход игрока {listOfXO[turn]}\nВыбери квадрант 1 - 9: ')
#                 except ValueError:
#                     await message.answer(f'Ход игрока {listOfXO[turn]}\nВыбери квадрант 1 - 9: ')
#             if listOfPosition[player - 1] == 0:
#                 check = True
#             else:
#                 await message.answer('\nПозиция занята!\n')
#         playersList[turn - 1].append(player)
#         for i in forWin:
#             if all(j in playersList[turn - 1] for j in i):
#                 await message.answer(f'\n Игрок {listOfXO[turn]} победил!')
#         listOfPosition[player - 1] = turn
#         turn = turn%2 + 1 
#         count+=1

#     await message.answer('\n Победила дружба!')

