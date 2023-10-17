from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_time_zodiac():
    keyboard_time = InlineKeyboardBuilder()
    keyboard_time.button(text='Вчера',
                         callback_data='yesterday')
    keyboard_time.button(text='Сегодня',
                         callback_data='today')
    keyboard_time.button(text='Завтра',
                         callback_data='tomorrow')
    keyboard_time.button(text='Неделя',
                         callback_data='week')
    keyboard_time.button(text='Месяц',
                         callback_data='month')
    keyboard_time.adjust(2)
    return keyboard_time.as_markup()


def get_zodiac_button():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Овен',
                            callback_data='aries')
    keyboard_builder.button(text='Телец',
                            callback_data='taurus')
    keyboard_builder.button(text='Близнецы',
                            callback_data='gemini')
    keyboard_builder.button(text='Рак',
                            callback_data='cancer')
    keyboard_builder.button(text='Лев',
                            callback_data='leo')
    keyboard_builder.button(text='Дева',
                            callback_data='virgo')
    keyboard_builder.button(text='Весы',
                            callback_data='libra')
    keyboard_builder.button(text='Скорпион',
                            callback_data='scorpio')
    keyboard_builder.button(text='Стрелец',
                            callback_data='sagittarius')
    keyboard_builder.button(text='Козерог',
                            callback_data='capricorn')
    keyboard_builder.button(text='Водолей',
                            callback_data='aquarius')
    keyboard_builder.button(text='Рыбы',
                            callback_data='pisces')
    keyboard_builder.button(text='Вернуться назад',
                            callback_data='back')
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()
