from dataclasses import dataclass
from environs import Env
from bs4 import BeautifulSoup
from lexicon.lexicon import headers
import httpx


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))


async def get_response(link: str):
    async with httpx.AsyncClient(headers=headers, follow_redirects=True) as htx:
        result: httpx.Response = await htx.get(url=link)
        if result.status_code != 200:
            return await get_response(link=link)
        else:
            return await result.aread()


async def get_text_horoscope(zodiac: str, day: str):
    link = f'https://horo.mail.ru/prediction/{zodiac}/{day}/'
    response_result = await get_response(link=link)
    beautifulsoup: BeautifulSoup = BeautifulSoup(markup=response_result, features='lxml')
    text = beautifulsoup.find(name='div', class_='article__text')
    return text.text
