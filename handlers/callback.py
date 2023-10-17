from aiogram import Router, F
from aiogram.types import CallbackQuery
from config_data.config import get_text_horoscope
from keyboards import inline_keyboard
from lexicon.lexicon import LEXICON_RU

router = Router()
day = ''


@router.callback_query(F.data.in_(['yesterday',
                                   'today',
                                   'tomorrow',
                                   'month',
                                   'week']))
async def get_day_horoscope(callback: CallbackQuery):
    global day
    await callback.answer()
    day = callback.data
    await callback.message.answer(text='Выбери нужный тебе знак зодиака!',
                                  reply_markup=inline_keyboard.get_zodiac_button())


@router.callback_query(F.data == 'back')
async def back_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text=LEXICON_RU['/start'],
                                  reply_markup=inline_keyboard.get_time_zodiac())


@router.callback_query()
async def get_horoscope(callback: CallbackQuery):
    global day
    await callback.answer()
    zodiac = callback.data
    text = await get_text_horoscope(zodiac=zodiac, day=day)
    await callback.message.answer(text=text,
                                  reply_markup=inline_keyboard.get_zodiac_button())
