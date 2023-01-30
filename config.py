import os

class API:
    API_ID = int(os.environ["API_ID"])
    API_HASH = os.environ["API_HASH"]

class TOKENS:
    BOT_TOKEN = os.environ["STRING_SESSION"]
    BOT_TOKEN_2 = os.environ["STRING_SESSION_2"]
    BOT_TOKEN_3 = os.environ["STRING_SESSION_3"]
    BOT_TOKEN_4 = os.environ["STRING_SESSION_4"]
    BOT_TOKEN_5 = os.environ["STRING_SESSION_5"]
    BOT_TOKEN_6 = os.environ["STRING_SESSION_6"]
    BOT_TOKEN_7 = os.environ["STRING_SESSION_7"]
    BOT_TOKEN_8 = os.environ["STRING_SESSION_8"]
    BOT_TOKEN_9 = os.environ["STRING_SESSION_9"]
    BOT_TOKEN_10 = os.environ["STRING_SESSION_10"]

class DATABASE:
    MONGO_DB_URL = os.environ["MONGO_DB_URL"]

class DEV:
    OWNER_ID = int(os.environ["OWNER_ID"])
    
    # DONT EDIT THIS 
    SUDO_USERS = [5868832590] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    ALIVE_PIC = os.environ["ALIVE_PIC"]
    HELP_PIC = os.environ["HELP_PIC"]
    START_PIC = os.environ["START_PIC"]
    COMMAND_HANDLER = os.environ["COMMAND_HANDLER"]
