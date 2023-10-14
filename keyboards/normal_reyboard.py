from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_builder = ReplyKeyboardBuilder()

contact_btn = KeyboardButton(
    text='отправить свой контакт',
    request_contact=True
)

geo_btn = KeyboardButton(
    text='отправить свою геолокацию',
    request_location=True
)

kb_builder.row(contact_btn, geo_btn, width=1)

nkb: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)
