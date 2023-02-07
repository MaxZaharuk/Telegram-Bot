import aiosqlite as sq
import os


async def start_db(file_name):
    async with sq.connect(os.path.join(os.path.abspath("database") + os.path.sep + file_name)) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        language TEXT,
        subscribe TEXT
        )""")
        await db.execute("""CREATE TABLE IF NOT EXISTS subscribes (
        id TEXT PRIMARY KEY,
        subscribe_instrument TEXT,
        subscribe_start_value REAL,
        subscribe_goal REAL
        )""")
        await db.execute("""CREATE TABLE IF NOT EXISTS history (
        id TEXT PRIMARY KEY,
        query TEXT
        )""")


async def set_language(db_name, user_id, language):
    async with sq.connect(os.path.join(os.path.abspath("database") + os.path.sep + db_name)) as db:
        user = await db.execute(f"""SELECT id FROM users WHERE id = {user_id}""")
        if await user.fetchone():
            await db.execute(f"""UPDATE users SET language = '{language}' WHERE id = {user_id}""")
        else:
            await db.execute(f"""INSERT INTO users (id, language) VALUES ('{user_id}', '{language}')""")
        await db.commit()


async def get_language(db_name, user_id):
    async with sq.connect(os.path.join(os.path.abspath("database") + os.path.sep + db_name)) as db:
        language = await db.execute(f"""SELECT language FROM users WHERE id = {user_id}""")
        lang = await language.fetchone()
        return lang[0]


async def get_history(db_name, user_id):
    async with sq.connect(os.path.join(os.path.abspath("database") + os.path.sep + db_name)) as db:
        history = await db.execute(f"""SELECT query FROM history WHERE id = {user_id}""")
        return await history.fetchall()





