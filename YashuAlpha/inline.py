
from pyrogram.types import InlineQueryResultPhoto as IQRP
from config import HELP_PIC
from .plugins import SPARE, HELP_TEXT, HELP_MARKUP

if not HELP_PIC:
    HELP_PIC = SPARE

ans = [IQRP(photo_url=HELP_PIC, thumb_url=SPARE, title="Help", description="Help Module [SPL-UB]", caption=HELP_TEXT, reply_markup=HELP_MARKUP)]

async def inl(_, i):
    text = i.query.lower()
    try:
        if text == "inline_help":
            await _.answer_inline_query(i.id, results=ans, cache_time=0)     
    except Exception as e:
        print(e)
