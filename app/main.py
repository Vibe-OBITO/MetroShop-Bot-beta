# /app/main.py

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import aiosqlite
import os

API_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я бот для продажи вещей в Metro Royale. Доступные команды:\n"
                        "/catalog - Просмотр каталога\n"
                        "/sets - Просмотр готовых наборов\n"
                        "/cart - Просмотр корзины\n"
                        "/addtocart - Добавить предмет в корзину")


@dp.message_handler(commands=['catalog'])
async def cmd_catalog(message: types.Message):
    async with aiosqlite.connect("shop.db") as db:
        async with db.execute("SELECT name, price FROM items") as cursor:
            items = await cursor.fetchall()

    catalog_message = "Каталог товаров:\n"
    for item in items:
        catalog_message += f"{item[0]} - {item[1]} монет\n"
    await message.reply(catalog_message)


@dp.message_handler(commands=['sets'])
async def cmd_sets(message: types.Message):
    async with aiosqlite.connect("shop.db") as db:
        async with db.execute("SELECT name FROM sets") as cursor:
            sets = await cursor.fetchall()

    sets_message = "Готовые наборы:\n"
    for s in sets:
        sets_message += f"{s[0]}\n"
    await message.reply(sets_message)


@dp.message_handler(commands=['addtocart'])
async def cmd_addtocart(message: types.Message):
    user_id = message.from_user.id
    item_name = ' '.join(message.get_args().split())

    async with aiosqlite.connect("shop.db") as db:
        async with db.execute("SELECT id FROM items WHERE name = ?", (item_name,)) as cursor:
            item = await cursor.fetchone()

        if item:
            item_id = item[0]
            await db.execute(
                "INSERT INTO carts (user_id, item_id, quantity) VALUES (?, ?, 1) ON CONFLICT(user_id, item_id) DO UPDATE SET quantity = quantity + 1",
                (user_id, item_id))
            await db.commit()
            await message.reply(f"Предмет '{item_name}' добавлен в корзину.")
        else:
            await message.reply("Предмет не найден.")


@dp.message_handler(commands=['cart'])
async def cmd_cart(message: types.Message):
    user_id = message.from_user.id

    async with aiosqlite.connect("shop.db") as db:
        async with db.execute("""
        SELECT items.name, carts.quantity, items.price
        FROM carts
        JOIN items ON carts.item_id = items.id
        WHERE carts.user_id = ?
        """, (user_id,)) as cursor:
            cart_items = await cursor.fetchall()

    if cart_items:
        cart_message = "Ваша корзина:\n"
        total = 0
        for item in cart_items:
            cart_message += f"{item[0]} - {item[1]} шт. - {item[2]} монет/шт.\n"
            total += item[1] * item[2]
        cart_message += f"Итого: {total} монет"
        await message.reply(cart_message)
    else:
        await message.reply("Ваша корзина пуста.")


if __name__ == '__main__':
    from aiogram import executor
    from db import create_tables


    async def on_startup(dp):
        await create_tables()


    executor.start_polling(dp, on_startup=on_startup)
