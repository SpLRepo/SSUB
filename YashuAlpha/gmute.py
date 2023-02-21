from .Database.gmute import *
from pyrogram import Client, filters
from .verify import verify
from . import hl, get_id_and_args
from pyrogram.types import ChatPermissions

@Client.on_message(filters.command("gmute", hl))
async def muter(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        id, args = get_id_and_args(_, m)
    except:
        return await m.reply("Invalid User !")
    if await verify(id):
        return await m.reply("Can't gmute sudo users !")
    if await is_gmuted(id):
        return await m.reply("User is already gmuted !")
    await gmute(id)
    await m.reply(f"Gmuted `{id}`."

@Client.on_message(filters.command("ungmute", hl))
async def unmuter(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        id, args = get_id_and_args(_, m)
    except:
        return await m.reply("Invalid User !")
    if not await is_gmuted(id):
        return await m.reply("User haven't been muted !")
    await ungmute(id)
    await m.reply(f"Ungmuted `{id}`."

@Client.on_message(group=10)
async def cwf(_, m):
    if not m.from_user:
        return
    id = m.from_user.id
    if not await is_gmuted(id):
        return
    try:
        await _.restrict_chat_member(m.chat.id, id, ChatPermissions())
        return await m.reply("User have been muted due to gmute !")
    except:
        try:
            await m.delete()
        except:
            pass
