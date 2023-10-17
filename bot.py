import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers, callback
from keyboards import set_menu


async def main() -> None:
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    await set_menu.set_main_menu(bot)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    dp.include_router(callback.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
