
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_TOKEN, API_ID, API_HASH, OWNER_ID, ADMINS, START_MSG, DB_URL, DB_NAME
from pymongo import MongoClient

# Logger Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pyrogram Client
app = Client(
    "AnimeMonarchBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# MongoDB Connection
mongo_client = MongoClient(DB_URL)
db = mongo_client[DB_NAME]
user_collection = db["users"]

# Start Command
@app.on_message(filters.command("start") & filters.private)
async def start(bot, message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    mention = f"<a href='tg://user?id={user_id}'>{first_name}</a>"
    
    # Add User to Database
    if not user_collection.find_one({"user_id": user_id}):
        user_collection.insert_one({"user_id": user_id, "first_name": first_name})
        logger.info(f"New User Joined: {user_id} | {first_name}")

    # Send Start Message
    await message.reply_text(
        START_MSG.format(first=first_name, id=user_id), 
        parse_mode="HTML"
    )

# Owner Command
@app.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def stats(bot, message: Message):
    total_users = user_collection.count_documents({})
    await message.reply_text(f"Total Users: {total_users}")

# Run Bot
if __name__ == "__main__":
    app.run()
