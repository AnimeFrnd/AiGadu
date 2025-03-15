
from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH
from bot import app
import handlers

# Main Bot Client
bot = Client(
    "AnimeMonarchBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Start the Bot
if __name__ == "__main__":
    print("🔥 Anime Monarch Auto-Post Bot Started Successfully! 👑")
    bot.run()
