
import os
import logging
from logging.handlers import RotatingFileHandler

def get_int_env(var_name, default):
    try:
        return int(os.environ.get(var_name, default))
    except ValueError:
        return default  # Fallback to default if conversion fails

def str_to_bool(value):
    return str(value).lower() in ("true", "1", "yes")

# Bot Credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5800464701:AAFfKXUNR_FaQqTQEDAEzeRZhHDLl5Ml9Ro")
API_ID = get_int_env("API_ID", 7515868)
API_HASH = os.environ.get("API_HASH", "dbd251e9ad4883b0443cc82b618ac6fa")

# Owner & Database Info
OWNER_ID = get_int_env("OWNER_ID", 6081617163)
DB_URL = os.environ.get("DB_URL", "mongodb+srv://bestanimeandcartoonsclips:6ChCTALD96W7qkps@cluster0.dt9r1rc.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "aryabro")

# Force Sub Channels (4 Working)
CHANNEL_ID = get_int_env("CHANNEL_ID", -1002292066966)
FORCE_SUB_CHANNEL = get_int_env("FORCE_SUB_CHANNEL", 0)
FORCE_SUB_CHANNEL2 = get_int_env("FORCE_SUB_CHANNEL2", 0)
FORCE_SUB_CHANNEL3 = get_int_env("FORCE_SUB_CHANNEL3", 0)
FORCE_SUB_CHANNEL4 = get_int_env("FORCE_SUB_CHANNEL4", 0)

# Other Settings
FILE_AUTO_DELETE = get_int_env("FILE_AUTO_DELETE", 86400)
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = get_int_env("TG_BOT_WORKERS", 6)

# Images
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/703f6dd8194cb5d707d63-c4bfc450283f9a4b4b.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/703f6dd8194cb5d707d63-c4bfc450283f9a4b4b.jpg")

# Admins Handling
ADMINS = {OWNER_ID}
env_admins = os.environ.get("ADMINS", "").split()
ADMINS.update(int(x) for x in env_admins if x.isdigit())
ADMINS = list(ADMINS)

# Custom Settings
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = str_to_bool(os.environ.get('PROTECT_CONTENT', "False"))
DISABLE_CHANNEL_BUTTON = str_to_bool(os.environ.get('DISABLE_CHANNEL_BUTTON', "True"))

# Start Message with User Quote
START_MSG = os.environ.get("START_MESSAGE", """<b><blockquote>
Hᴇʏ, <a href='tg://user?id={id}'>{first}</a>✌🏻. I ʜᴏᴘᴇ ʏᴏᴜ'ʀᴇ ғᴇᴇʟɪɴɢ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏғ 𝐒ʜᴀᴅᴏᴡ Mᴏɴᴀʀᴄʜ 😈.

I'ᴍ 𝐓ʜᴇ Uʟᴛɪᴍᴀᴛᴇ Fɪʟᴇ Sʜᴀʀɪɴɢ Bᴏᴛ, ʙᴜɪʟᴛ ᴛᴏ ʀᴜʟᴇ ᴛʜᴇ 𝐒ʜᴀᴅᴏᴡ Rᴇᴀʟᴍ 🖤

🔱 Sᴛᴏʀᴇ & Sʜᴀʀᴇ Fɪʟᴇs ᴡɪᴛʜ ᴀ Sɪɴɢʟᴇ Cʟɪᴄᴋ.  
🛡️ Iɴꜰɪɴɪᴛᴇ Fɪʟᴇ Mᴀɴᴀɢᴇᴍᴇɴᴛ Sʏꜱᴛᴇᴍ.  
📂 Pᴏsᴛ Fɪʟᴇs ɪɴ 𝐀ɴɪᴍᴇ Mᴏɴᴀʀᴄʜ 👑 Tᴇᴍᴘʟᴀᴛᴇ.

---

𝐍ᴏᴡ, 𝐓ʜᴇ Fɪʟᴇ Rᴇᴀʟᴍ Iꜱ Uɴᴅᴇʀ Mʏ Cᴏɴᴛʀᴏʟ 😈.  
𝐀ʀᴇ Yᴏᴜ Rᴇᴀᴅʏ ᴛᴏ Dᴏᴍɪɴᴀᴛᴇ, {first}-Sᴀᴍᴀ? 👑
</blockquote></b>""")

# Logger Setup
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
