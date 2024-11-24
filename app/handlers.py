from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboads as kb

router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text='Приветствую, выбери, что хочешь сделать', reply_markup=kb.main)

@router.message(F.text == 'Набрать массу')
async def mass(message: Message):
    await message.answer(text='Укажи массу своего тела', reply_markup=kb.mass_keyboard)