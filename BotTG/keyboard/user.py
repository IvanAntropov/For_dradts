from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Start, /help')
b2 = KeyboardButton('/cat')
b3 = KeyboardButton('/who')

kb_user = ReplyKeyboardMarkup(resize_keyboard=True)  #  one_time_keyboard=True, ReplyKeyboardRemove

kb_user.add(b1).add(b2).insert(b3)

# kb_user.row(b1,b2,b3)

