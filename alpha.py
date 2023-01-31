from pyrogram import Client, filters, idle
from config import *
import time
from YashuAlpha.plugins import start, help, cmds_cbq, close_cbq, raid_cbq, extra_cbq, spam_cbq
from YashuAlpha.raid import raid, replyraid, dreplyraid, raid_cwf
from YashuAlpha.data import KeshavX
from YashuAlpha.spam import spam_func, dspam_func, spam_stop
from YashuAlpha.echo import addecho, rmecho, echo_cwf, echos
from YashuAlpha.leave import leave
from YashuAlpha.sudo import add_or_del_sudo, sudo_users
from YashuAlpha.alive_ping import ping, aliver 
from YashuAlpha.inline import inl
import sys
from external_client import BOT

hl = STUFF.COMMAND_HANDLER

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + KeshavX

LEGEND = DEV.OWNER_ID

if not BOT:
    print("BOT TOKEN NOT FOUND, ADD IT TO INITIATE !")
    sys.exit()
if not STRING_SESSION:
    print("MAIN STRING NOT FOUND, ADD IT TO INITIATE !")
    sys.exit()
END = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION)
if STRING_SESSION_2:
    END2 = Client(":END2:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_2)
if STRING_SESSION_3:
    END3 = Client(":END3:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_3)
if STRING_SESSION_4:
    END4 = Client(":END4:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_4)
if STRING_SESSION_5:
    END5 = Client(":END5:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_5)
if STRING_SESSION_6:
    END6 = Client(":END6:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_6)
if STRING_SESSION_7:
    END7 = Client(":END7:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_7)
if STRING_SESSION_8:
    END8 = Client(":END8:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_8)
if STRING_SESSION_9:
    END9 = Client(":END9:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_9)
if STRING_SESSION_10:
    END10 = Client(":END10:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION_10)

@END.on_message(filters.command("help", hl))
@END2.on_message(filters.command("help", hl))
@END3.on_message(filters.command("help", hl))
@END4.on_message(filters.command("help", hl))
@END5.on_message(filters.command("help", hl))
@END6.on_message(filters.command("help", hl))
@END7.on_message(filters.command("help", hl))
@END8.on_message(filters.command("help", hl))
@END9.on_message(filters.command("help", hl))
@END10.on_message(filters.command("help", hl))
async def help_plug(_, m):
    await help(_, m)

print("[module] loaded :- help")

@END.on_message(filters.command("ping", hl))
@END2.on_message(filters.command("ping", hl))
@END3.on_message(filters.command("ping", hl))
@END4.on_message(filters.command("ping", hl))
@END5.on_message(filters.command("ping", hl))
@END6.on_message(filters.command("ping", hl))
@END7.on_message(filters.command("ping", hl))
@END8.on_message(filters.command("ping", hl))
@END9.on_message(filters.command("ping", hl))
@END10.on_message(filters.command("ping", hl))
async def ping_plug(_, m):
    await ping(_, m)

print("\n[module] loaded :- ping")

@END.on_message(filters.command("alive", hl))
@END2.on_message(filters.command("alive", hl))
@END3.on_message(filters.command("alive", hl))
@END4.on_message(filters.command("alive", hl))
@END5.on_message(filters.command("alive", hl))
@END6.on_message(filters.command("alive", hl))
@END7.on_message(filters.command("alive", hl))
@END8.on_message(filters.command("alive", hl))
@END9.on_message(filters.command("alive", hl))
@END10.on_message(filters.command("alive", hl))
async def alive_plug(_, m):
    await aliver(_, m)

print("[module] loaded :- alive")

@END.on_message(filters.command("spam", hl))
@END2.on_message(filters.command("spam", hl))
@END3.on_message(filters.command("spam", hl))
@END4.on_message(filters.command("spam", hl))
@END5.on_message(filters.command("spam", hl))
@END6.on_message(filters.command("spam", hl))
@END7.on_message(filters.command("spam", hl))
@END8.on_message(filters.command("spam", hl))
@END9.on_message(filters.command("spam", hl))
@END10.on_message(filters.command("spam", hl))
async def spam_plug(_, m):
    await spam_func(_, m)

print("\n[module] loaded :- spam")

@END.on_message(filters.command("dspam", hl))
@END2.on_message(filters.command("dspam", hl))
@END3.on_message(filters.command("dspam", hl))
@END4.on_message(filters.command("dspam", hl))
@END5.on_message(filters.command("dspam", hl))
@END6.on_message(filters.command("dspam", hl))
@END7.on_message(filters.command("dspam", hl))
@END8.on_message(filters.command("dspam", hl))
@END9.on_message(filters.command("dspam", hl))
@END10.on_message(filters.command("dspam", hl))
async def dspam_plug(_, m):
    await dspam_func(_, m)

print("\n[module] loaded :- dspam")

@END.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(LEGEND))
async def sudo_plug(_, m):
    await add_or_del_sudo(_, m)

@END.on_message(filters.command("sudos", hl))
@END2.on_message(filters.command("sudos", hl))
@END3.on_message(filters.command("sudos", hl))
@END4.on_message(filters.command("sudos", hl))
@END5.on_message(filters.command("sudos", hl))
@END6.on_message(filters.command("sudos", hl))
@END7.on_message(filters.command("sudos", hl))
@END8.on_message(filters.command("sudos", hl))
@END9.on_message(filters.command("sudos", hl))
@END10.on_message(filters.command("sudos", hl))
async def gsudo_plug(_, m):
    await sudo_users(_, m)

print("\n[module] loaded :- sudos")

@END.on_message(filters.command("addecho", hl))
async def addecho_plug(_, m):
    await addecho(_, m)

print("\n[module] loaded :- addecho")

@END.on_message(filters.command("rmecho", hl))
async def rmecho_plug(_, m):
    await rmecho(_, m)

print("\n[module] loaded :- rmecho")

@END.on_message(filters.command("echos", hl))
@END2.on_message(filters.command("echos", hl))
@END3.on_message(filters.command("echos", hl))
@END4.on_message(filters.command("echos", hl))
@END5.on_message(filters.command("echos", hl))
@END6.on_message(filters.command("echos", hl))
@END7.on_message(filters.command("echos", hl))
@END8.on_message(filters.command("echos", hl))
@END9.on_message(filters.command("echos", hl))
@END10.on_message(filters.command("echos", hl))
async def echos_plug(_, m):
    await echos(_, m)

@END.on_message(filters.command("stop", hl))
@END2.on_message(filters.command("stop", hl))
@END3.on_message(filters.command("stop", hl))
@END4.on_message(filters.command("stop", hl))
@END5.on_message(filters.command("stop", hl))
@END6.on_message(filters.command("stop", hl))
@END7.on_message(filters.command("stop", hl))
@END8.on_message(filters.command("stop", hl))
@END9.on_message(filters.command("stop", hl))
@END10.on_message(filters.command("stop", hl))
async def stop_plug(_, m):
    await spam_stop(_, m)

@END.on_message(filters.command("raid", hl))
@END2.on_message(filters.command("raid", hl))
@END3.on_message(filters.command("raid", hl))
@END4.on_message(filters.command("raid", hl))
@END5.on_message(filters.command("raid", hl))
@END6.on_message(filters.command("raid", hl))
@END7.on_message(filters.command("raid", hl))
@END8.on_message(filters.command("raid", hl))
@END9.on_message(filters.command("raid", hl))
@END10.on_message(filters.command("raid", hl))
async def raid_plug(_, m):
    await raid(_, m)

print("\n[module] loaded :- raid")

@END.on_message(filters.command("replyraid", hl))
async def replyraid_plug(_, m):
    await replyraid(_, m)

print("\n[module] loaded :- replyraid")

@END.on_message(filters.command("dreplyraid", hl))
async def dreplyraid_plug(_, m):
    await dreplyraid(_, m)

print("\n[module] loaded :- dreplyraid")

@END.on_message(filters.command("leave", hl))
@END2.on_message(filters.command("leave", hl))
@END3.on_message(filters.command("leave", hl))
@END4.on_message(filters.command("leave", hl))
@END5.on_message(filters.command("leave", hl))
@END6.on_message(filters.command("leave", hl))
@END7.on_message(filters.command("leave", hl))
@END8.on_message(filters.command("leave", hl))
@END9.on_message(filters.command("leave", hl))
@END10.on_message(filters.command("leave", hl))
async def leave_plug(_, m):
    await leave(_, m)

print("\n[module] loaded :- leave")

@BOT.on_message(filters.command("start", [hl, "/"]))
async def start_plug(_, m):
    await start(_, m)

print("\n[module] loaded :- start")

@BOT.on_callback_query(filters.regex("cmds"))
async def cmds_cbq_plug(_, q):
    await cmds_cbq(_, q)

print("\n[module] loaded :- cmds_cbq")

@BOT.on_callback_query(filters.regex("spam"))
async def spam_cbq_plug(_, q):
    await spam_cbq(_, q)

print("\n[module] loaded :- spam_cbq")

@BOT.on_callback_query(filters.regex("raid"))
async def raid_cbq_plug(_, q):
    await raid_cbq(_, q)

print("\n[module] loaded :- raid_cbq")

@BOT.on_callback_query(filters.regex("extra"))
async def extra_cbq_plug(_, q):
    await extra_cbq(_, q)

print("\n[module] loaded :- extra_cbq")

@BOT.on_callback_query(filters.regex("close"))
async def close_cbq_plug(_, q):
    await close_cbq(_, q)

print("\n[module] loaded :- close_cbq")

@BOT.on_inline_query()
async def inli(_, i):
    await inl(_, i)

@END.on_message(group=1)
@END2.on_message(group=1)
@END3.on_message(group=1)
@END4.on_message(group=1)
@END5.on_message(group=1)
@END6.on_message(group=1)
@END7.on_message(group=1)
@END8.on_message(group=1)
@END9.on_message(group=1)
@END10.on_message(group=1)
async def echo_cwf_plug(_, m):
    await echo_cwf(_, m)

print("\n[module] loaded :- echo_cwf")

@END.on_message(group=2)
@END2.on_message(group=2)
@END3.on_message(group=2)
@END4.on_message(group=2)
@END5.on_message(group=2)
@END6.on_message(group=2)
@END7.on_message(group=2)
@END8.on_message(group=2)
@END9.on_message(group=2)
@END10.on_message(group=2)
async def raid_cwf_plug(_, m):
    await raid_cwf(_, m)

print("\n[module] loaded :- raid_cwf")

BOT.start()
print("Bot started, enable inline mode if not enabled !")
print("Starting User Clients...")
END.start()
END.join("splbots")
END.join("coding_bots")
print("\nEND1 STARTED !")
if STRING_SESSION_2:
    END2.start()
    print("\nEND2 STARTED !")
if STRING_SESSION_3:
    END3.start()
    print("\nEND3 STARTED !")
if STRING_SESSION_4:
    END4.start()
    print("\nEND4 STARTED !")
if STRING_SESSION_5:
    END5.start()
    print("\nEND5 STARTED !")
if STRING_SESSION_6:
    END6.start()
    print("\nEND6 STARTED !")
if STRING_SESSION_7:
    END7.start()
    print("\nEND7 STARTED !")
if STRING_SESSION_8:
    END8.start()
    print("\nEND8 STARTED !")
if STRING_SESSION_9:
    END9.start()
    print("\nEND9 STARTED !")
if STRING_SESSION_10:
    END10.start()
    print("\nEND10 STARTED !")
CLIENTS = [END2, END3, END4, END5, END6, END7, END8, END9, END10]
for x in CLIENTS:
    try:
        if x:
            x.join("splbots")
            x.join("coding_bots")
    except:
        pass
print("\n\nALL CLIENTS STARTED SUCCESSFULLY !\nJoin @SpLBots")
idle()
