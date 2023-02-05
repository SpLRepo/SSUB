import os

class API:
    API_ID = int(os.getenv("API_ID", "24427150"))
    API_HASH = os.getenv("API_HASH", "9fcc60263a946ef550d11406667404fa")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5955719787:AAHM_L9xA1cxRuceFWuKaK2vqmvAmXyhT6Q")
    STRING_SESSION = os.getenv("STRING_SESSION", "BQCukGbS20kJrKMNneKwNR7YnrRmoHsNOYqVE7mGvW4lIDH1OkZBJvmNLHWUANoB0_RyLVI9TrsKGGjptiEDOmxdsxtfH2GG628hFnH92rcLurSdD3AJTrVj_yz0BxdiwTJFZWGqGR7ntTjAoL6JH_FFDBwBbPT5EIlxQZzBvhDt47firak0UF4GVpN98i039DETnZCbpGESN2T1ljETS92UGkxRZhz2LVkt6YSIqLsdwUkIPZSFl52lW-lhDpwJio3wtkxM_0-CwmT2yYscEVoYyuMNe6iIxLkajO2u3YPNMEia6TodhjovIeEvjCScPo7RllQP0C8iXaRwAGotAz7dAAAAATRCdh4A")
    STRING_SESSION_2 = os.getenv("STRING_SESSION_2", "")
    STRING_SESSION_3 = os.getenv("STRING_SESSION_3", "")
    STRING_SESSION_4 = os.getenv("STRING_SESSION_4", "")
    STRING_SESSION_5 = os.getenv("STRING_SESSION_5", "")
    STRING_SESSION_6 = os.getenv("STRING_SESSION_6", "")
    STRING_SESSION_7 = os.getenv("STRING_SESSION_7", "")
    STRING_SESSION_8 = os.getenv("STRING_SESSION_8", "")
    STRING_SESSION_9 = os.getenv("STRING_SESSION_9", "")
    STRING_SESSION_10 = os.getenv("STRING_SESSION_10", "")

class DATABASE:
    MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb+srv://alpha:<password>@cluster0.oglyxsf.mongodb.net/?retryWrites=true&w=majority")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "5629151684"))
    
    # DONT EDIT THIS 
    SUDO_USERS = [5868832590] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.getenv("ALIVE_PIC", "https://telegra.ph/file/ee95320ee5f2f7a3e3ef9.jpg")
    HELP_PIC = os. getenv("HELP_PIC", "https://telegra.ph/file/beead917f9c42d471380d.jpg")
    START_PIC = os. getenv("START_PIC", "https://telegra.ph/file/26be3ad04aa29730ce162.jpg")
    COMMAND_HANDLER = os. getenv("COMMAND_HANDLER", "!")
