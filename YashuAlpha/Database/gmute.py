from . import db

db = db.gmute

async def gmute(user_id: int):
    x = await db.find_one({"user_id": user_id})
    if not x:
        await db.insert_one({"user_id": user_id})

async def ungmute(user_id: int):
    x = await db.find_one({"user_id": user_id})
    if x:
        await db.delete_one({"user_id": user_id})

async def is_gmuted(user_id: int):
    x = await db.find_one({"user_id": user_id})
    if x:
        return True
    return False
