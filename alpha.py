from pyrogram import Client, filters, idle
from config import *
import time
import sys
from external_client import BOT
from alphagram import Alpha

if not BOT:
    print("BOT TOKEN NOT FOUND, ADD IT TO INITIATE !")
    sys.exit()
if not TOKENS.STRING_SESSION:
    print("MAIN STRING NOT FOUND, ADD IT TO INITIATE !")
    sys.exit()
END = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION, plugins=dict(root="YashuAlpha"))
if TOKENS.STRING_SESSION_2:
    END2 = Client(":END2:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_2, plugins=dict(root="YashuAlpha"))
else:
    END2 = None
if TOKENS.STRING_SESSION_3:
    END3 = Client(":END3:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_3, plugins=dict(root="YashuAlpha"))
else:
    END3 = None
if TOKENS.STRING_SESSION_4:
    END4 = Client(":END4:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_4, plugins=dict(root="YashuAlpha"))
else:
    END4 = None
if TOKENS.STRING_SESSION_5:
    END5 = Client(":END5:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_5, plugins=dict(root="YashuAlpha"))
else:
    END5 = None
if TOKENS.STRING_SESSION_6:
    END6 = Client(":END6:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_6, plugins=dict(root="YashuAlpha"))
else:
    END6 = None
if TOKENS.STRING_SESSION_7:
    END7 = Client(":END7:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_7, plugins=dict(root="YashuAlpha"))
else:
    END7 = None
if TOKENS.STRING_SESSION_8:
    END8 = Client(":END8:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_8, plugins=dict(root="YashuAlpha"))
else:
    END8 = None
if TOKENS.STRING_SESSION_9:
    END9 = Client(":END9:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_9, plugins=dict(root="YashuAlpha"))
else:
    END9 = None
if TOKENS.STRING_SESSION_10:
    END10 = Client(":END10:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_10, plugins=dict(root="YashuAlpha"))
else:
    END10 = None

BOT.start()
print("Bot started, enable inline mode if not enabled !")
print("Starting User Clients...")
END.start()
try:
    END.join_chat("splbots")
    END.join_chat("coding_bots")
except:
    pass
print("\nEND1 STARTED !")
if TOKENS.STRING_SESSION_2:
    END2.start()
    print("\nEND2 STARTED !")
if TOKENS.STRING_SESSION_3:
    END3.start()
    print("\nEND3 STARTED !")
if TOKENS.STRING_SESSION_4:
    END4.start()
    print("\nEND4 STARTED !")
if TOKENS.STRING_SESSION_5:
    END5.start()
    print("\nEND5 STARTED !")
if TOKENS.STRING_SESSION_6:
    END6.start()
    print("\nEND6 STARTED !")
if TOKENS.STRING_SESSION_7:
    END7.start()
    print("\nEND7 STARTED !")
if TOKENS.STRING_SESSION_8:
    END8.start()
    print("\nEND8 STARTED !")
if TOKENS.STRING_SESSION_9:
    END9.start()
    print("\nEND9 STARTED !")
if TOKENS.STRING_SESSION_10:
    END10.start()
    print("\nEND10 STARTED !")
CLIENTS = [END2, END3, END4, END5, END6, END7, END8, END9, END10]
a = 0
for x in CLIENTS:
    if x:
        a += 1
    else:
        continue
    try:
        x.join_chat("splbots")
        x.join_chat("coding_bots")
    except:
        pass

if a == 1:
    txt = "1 CLIENT"
else:
    txt = f"{a} CLIENTS"
print(f"\n\n{txt} STARTED SUCCESSFULLY !\nJoin @SpLBots")
idle()
