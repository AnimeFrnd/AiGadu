
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
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
API_ID = get_int_env("API_ID", 1234567)
API_HASH = os.environ.get("API_HASH", "YOUR_API_HASH_HERE")

# Owner & Database Info
OWNER_ID = get_int_env("OWNER_ID", 123456789)
DB_URL = os.environ.get("DB_URL", "YOUR_MONGODB_URI_HERE")
DB_NAME = os.environ.get("DB_NAME", "DATABASE_NAME")

# Force Sub Channels (4 Working)
CHANNEL_ID = get_int_env("CHANNEL_ID", -1001234567890)
FORCE_SUB_CHANNEL = get_int_env("FORCE_SUB_CHANNEL", -1001234567891)
FORCE_SUB_CHANNEL2 = get_int_env("FORCE_SUB_CHANNEL2", -1001234567892)
FORCE_SUB_CHANNEL3 = get_int_env("FORCE_SUB_CHANNEL3", -1001234567893)
FORCE_SUB_CHANNEL4 = get_int_env("FORCE_SUB_CHANNEL4", -1001234567894)

# Other Settings
FILE_AUTO_DELETE = get_int_env("FILE_AUTO_DELETE", 86400)
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = get_int_env("TG_BOT_WORKERS", 6)

# Images
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/example.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/example.jpg")

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
