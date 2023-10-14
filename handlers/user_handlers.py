from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from keyboards.normal_reyboard import nkb, ReplyKeyboardRemove

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=nkb)


@router.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['Собак 🦮'],
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
