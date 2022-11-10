# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types

import view
from bot import bot


async def start(message: types.Message):
    await view.greetings(message)

async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'до свидания!')
async def help(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'\n/help - вывод всех команд доступных боту'
                        f'\n/finish - выход из игры'
                        f'\n/rules - правила игры в конфетки'
                        f'\n/start - начало игры')
async def rules(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.' 
                        f'За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.' )

async def getNumber(message: types.Message):
    number = message.text
    if 0 < int(number) < 29:
        print(number)
    else:
        await bot.send_message(message.from_user.id, 'Ах, ты грязный читер!')