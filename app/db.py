# /app/db.py

import aiosqlite

async def create_tables():
    async with aiosqlite.connect("shop.db") as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        )
        """)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS carts (
            user_id INTEGER,
            item_id INTEGER,
            quantity INTEGER,
            PRIMARY KEY (user_id, item_id)
        )
        """)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS sets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS set_items (
            set_id INTEGER,
            item_id INTEGER,
            PRIMARY KEY (set_id, item_id)
        )
        """)
        await db.commit()

async def add_item(name, price, category):
    async with aiosqlite.connect("shop.db") as db:
        await db.execute("INSERT INTO items (name, price, category) VALUES (?, ?, ?)", (name, price, category))
        await db.commit()

# Запуск и создание таблиц
if __name__ == "__main__":
    import asyncio
    asyncio.run(create_tables())
    # Пример добавления предметов
    asyncio.run(add_item("Шлем 6 уровня", 5000, "экипировка"))
    asyncio.run(add_item("Рюкзак 6 уровня", 4500, "экипировка"))
    asyncio.run(add_item("Броня 6 уровня", 8000, "экипировка"))
