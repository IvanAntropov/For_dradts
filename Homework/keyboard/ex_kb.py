from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/ex1')
b2 = KeyboardButton('/ex2')
b3 = KeyboardButton('/ex3')
b4 = KeyboardButton('/ex4')
b5 = KeyboardButton('/ex5')
buttonEx = KeyboardButton('/exit')

kb1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)  #  one_time_keyboard=True, ReplyKeyboardRemove
kb2 = ReplyKeyboardMarkup(resize_keyboard=True)

kb1.row(b1,b2,b3,b4,b5).insert(buttonEx)
kb2.add(buttonEx)
