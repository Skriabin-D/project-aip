from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Набрать массу'), KeyboardButton(text='Подсушиться')],
    [KeyboardButton(text='Бухать'), KeyboardButton(text='Бухать и качаться')]
])

mass_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='< 40 kg', callback_data='low'), InlineKeyboardButton(text='40-70 kg', callback_data='middle')],
    [InlineKeyboardButton(text='> 70 kg', callback_data='high')]
])