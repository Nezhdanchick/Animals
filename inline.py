from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cats = InlineKeyboardButton(text='Котов', url='https://ru.wikipedia.org/wiki/Кошка')
dogs = InlineKeyboardButton(text='Собак', url='https://ru.wikipedia.org/wiki/Собака')

cats_dogs_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [cats, dogs]
])

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callback.animals import AnimalsCallback

cats = InlineKeyboardButton(text='Котов', callback_data=AnimalsCallback(animal='Кот', count=4).pack())
dogs = InlineKeyboardButton(text='Собак', callback_data=AnimalsCallback(animal='Собака', count=5).pack())
fish = InlineKeyboardButton(text='Рыб', callback_data=AnimalsCallback(animal='Рыба', count=1).pack())
owl = InlineKeyboardButton(text='Сов', callback_data=AnimalsCallback(animal='Сова', count=10).pack())

cats_dogs_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [cats, dogs],
    [fish, owl]
])
