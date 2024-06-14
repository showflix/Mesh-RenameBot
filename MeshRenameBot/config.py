from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://showflixuser:showflixuser@cluster0.mqv9zew.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"]
        API_HASH = [str, "a8d3503be0455c779a17193e48cab451"]
        API_ID = [int, 14959925]
        BOT_TOKEN = [str, "7174676764:AAFJGZBLpJCMwh19P509WZ-4o0w1CJR38t4"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 5]
        IS_MONGO = [bool, True]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[123456789]]
        OWNER_ID = [int, 0]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"https://t.me/showflix_movie"]
        FORCEJOIN_ID = [int,-1001792757301]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
