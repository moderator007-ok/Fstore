#(©)Codeflix_Bots

import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8126175037:AAFTqQUDOKjU4mdeFI7qSmQt-kmYU6Mmo1M")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23987350"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "571dcf3357698eb23a47eee729d164e1")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002488585826"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1415136344"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://XORG:XnPGfXfvGDa6j4Tm@captionbot.7hia2c3.mongodb.net/?retryWrites=true&w=majority&appName=captionbot")
DB_NAME = os.environ.get("DATABASE_NAME", "captionbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002370814979"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002297034064"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "0"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>HEY!! {first}\n\n I AM File Providing Bot MADE BY ORGSUPPORT, You can Access file shared by our Admin.</blockquote></b>")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1415136344").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} 𝐁𝐫𝐨/𝐒𝐢𝐬 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞.\n\n𝐉𝐨𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐭𝐡𝐞𝐧 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @ORGSupport</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Huh ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ Owner Bullshit!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @ORGSupport"

ADMINS.append(OWNER_ID)
ADMINS.append(1415136344)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Define the TIME variable
TIME = int(os.environ.get("TIME", "3600"))  # Default
