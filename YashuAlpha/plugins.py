from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import DEV, STUFF
import time
from .data import KeshavX
from external_client import BOT
from pyrogram import Client, filters
from external_client import BOT

hl = STUFF.COMMAND_HANDLER
from .verify import verify

SPARE = "https://telegra.ph/file/31f1906a790ec93ace4e2.jpg"

START_PIC = STUFF.START_PIC if STUFF.START_PIC else SPARE

HELP_PIC = STUFF.HELP_PIC if STUFF.HELP_PIC else SPARE

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + KeshavX

START_MARKUP_STR = IKM(
               [
               [
               IKB("💭 Owner 💭", url="t.me/NotKeshav"),
               IKB("✨ Support ✨", url="t.me/SpLBots")
               ],
               [
               IKB("🔥 Repo 🔥", url="https://github.com/ShutupKeshav/SpLSpamUserBot")
               ]
               ]
               )

START_MARKUP_DEV = IKM(
               [
               [
               IKB("💫 Commands 💫", callback_data="cmds"),
               IKB("💭 Support 💭", url="t.me/SpLBots")
               ]
               ]
               )  

@BOT.on_message(filters.command("start", [hl, "/"]))
async def start(_, m):
    DEV.SUDO_USERS.append(DEV.OWNER_ID)
    x = DEV.SUDO_USERS
    bot_name = "𝙎𝙥𝙇 𝙓 𝙎𝙥𝙖𝙢"
    if await verify(m.from_user.id):
        txt = f"**Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\n Click Below Buttons For Help. 🌚**"
        await m.reply_photo(START_PIC, caption=txt, reply_markup=START_MARKUP_DEV)
        return
    if str(m.chat.id)[0] == "-":
        return
    men = m.from_user.mention
    txt = f"**Hello !! {men}\nNice To Meet You, Well I Am {bot_name}, A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Given Below.** \n\n**Powered By : [𝙎𝙥𝙇](https://t.me/SpLBots)**"
    await m.reply_photo(START_PIC, caption=txt, reply_markup=START_MARKUP_STR)
    return

HELP_TEXT = "★ 𝙎𝙥𝙇 𝙓 𝙎𝙥𝙖𝙢 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩"

SPAM_HELP = spam_msg = f"""
**Help Spam Cmds**

**Spam :** Spams a Message For Given Counter(<= 100).
Command :
1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}spam <count> <replying any message>

**DelaySpam :** Delay Spam a Text For Given Counter After Given Time.
Command :
1) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}delayspam <delay> <count> <replying any message>

** © @NotKeshav**
"""

RAID_HELP = f"""
**Help Raid Cmds**

**Raid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}raid <count> <username
2) {hl}raid <count> <reply to user>

**ReplyRaid :** Activates Reply Raid on The User!!
Command :
1) {hl}replyraid <replying to user>
2) {hl}dreplyraid <username>

**DReplyRaid :** Deactivates Reply Raid on The User!!
Command :
1) {hl}dreplyraid <replying to user>
2) {hl}dreplyraid <username>


**© @NotKeshav**
"""

EXTRA_HELP = f"""
**Help Extra Cmds**

**Alive and Ping :** Ping Cmds
Command :
1) {hl}ping 
2) {hl}alive

**Echo :** To Active Echo On Any User
Command :
1) {hl}addecho <reply to user>
2) {hl}rmecho <reply to user>

**Leave:** To Leave Group/Channel
Command :
1) {hl}leave <group/chat id>
2) {hl}leave : Type in the Group bot will auto leave that group

**Join:** To Leave Group/Channel
Command :
1) {hl}Join <group/chat id>
2) {hl}Join : Type in the Group bots will join that group.

**© @NotKeshav**
"""

HELP_MARKUP = IKM(
              [
              [
              IKB("⚡️ Spam ⚡️", callback_data="spam"),
              IKB("🔥 Raid 🔥", callback_data="raid")
              ],
              [
              IKB("💭 Extras 💭", callback_data="extra")
              ],
              [
              IKB("😶‍🌫️ Owner 😶‍🌫️", url="t.me/NotKeshav"),
              IKB("✨ Support ✨", url="t.me/SpLBots")
              ]
              ]
              )
botun = None

@Client.on_message(filters.command("help", hl))
async def help(_, m):
    global botun
    if not botun:
        botun = (await BOT.get_me()).username
    if not await verify(m.from_user.id):
        return
    ok = await m.reply(" 🇮🇳 ")
    try:
        nice = await _.get_inline_bot_results(bot=botun, query="inline_help")
    except Exception as e:
        return await m.reply(e)
    try:
        await ok.delete()
        await m.delete()
    except:
        pass
    try:
        await _.send_inline_bot_result(m.chat.id, nice.query_id, nice.results[0].id)
    except Exception as e:
        await m.reply(e)

CLOSE_MARKUP = IKM(
               [
               [
               IKB("🗑️ Close", callback_data="close")
               ]
               ]
               )

@BOT.on_callback_query(filters.regex("cmds"))
async def cmds_cbq(_, q):
    if not await verify(q.from_user.id):
        return await q.answer("START ME IN PRIVATE AND GET SOURCE CODE OF THIS BOT ! AND DEPLOY YOUR OWN !", show_alert=True)
    await q.answer()
    await q.edit_message_text(text=HELP_TEXT, reply_markup=HELP_MARKUP)

@BOT.on_callback_query(filters.regex("spam"))
async def spam_cbq(_, q):
    if not await verify(q.from_user.id):
        return await q.answer("START ME IN PRIVATE AND GET SOURCE CODE OF THIS BOT ! AND DEPLOY YOUR OWN !", show_alert=True)
    await q.answer()
    await q.edit_message_text(text=SPAM_HELP, reply_markup=CLOSE_MARKUP)

@BOT.on_callback_query(filters.regex("raid"))
async def raid_cbq(_, q):
    if not await verify(q.from_user.id):
        return await q.answer("START ME IN PRIVATE AND GET SOURCE CODE OF THIS BOT ! AND DEPLOY YOUR OWN !", show_alert=True)
    await q.answer()
    await q.edit_message_text(text=RAID_HELP, reply_markup=CLOSE_MARKUP)

@BOT.on_callback_query(filters.regex("extra"))
async def extra_cbq(_, q):
    if not await verify(q.from_user.id):
        return await q.answer("START ME IN PRIVATE AND GET SOURCE CODE OF THIS BOT ! AND DEPLOY YOUR OWN !", show_alert=True)
    await q.answer()
    await q.edit_message_text(text=EXTRA_HELP, reply_markup=CLOSE_MARKUP)

@BOT.on_callback_query(filters.regex("close"))
async def close_cbq(_, q):
    if not await verify(q.from_user.id):
        return await q.answer("START ME IN PRIVATE AND GET SOURCE CODE OF THIS BOT ! AND DEPLOY YOUR OWN !", show_alert=True)
    await q.answer()
    await q.message.delete()

