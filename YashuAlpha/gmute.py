from .Database.gmute import *
from pyrogram import Client, filters
from .verify import verify

@Client.on_message(filters.command("gmute"))
