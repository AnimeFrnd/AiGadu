
from pyrogram import Client, filters
from pyrogram.types import Message
from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4, FILE_AUTO_DELETE
from database import add_user, is_user_exist, save_file, get_file, log_activity

# Force Subscribe
async def force_sub(bot, message: Message):
    user_id = message.from_user.id
    channels = [FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4]

    for channel in channels:
        try:
            member = await bot.get_chat_member(channel, user_id)
            if member.status in ["member", "administrator", "creator"]:
                continue
        except:
            await message.reply_text("⚡ Join Required Channel First!", quote=True)
            return False
    return True

# Handle New User
@app.on_message(filters.private & filters.command("start"))
async def handle_start(bot, message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    # Add User to DB
    add_user(user_id, first_name)

    # Force Sub Check
    if not await force_sub(bot, message):
        return

    await message.reply_text(f"Welcome, {first_name}! 👑", quote=True)

# Handle File Saving
@app.on_message(filters.private & filters.document | filters.video | filters.audio | filters.photo)
async def handle_files(bot, message: Message):
    user_id = message.from_user.id
    file_id = message.document.file_id if message.document else message.video.file_id
    file_name = message.document.file_name if message.document else "Unknown File"
    file_type = message.document.mime_type if message.document else "video/mp4"
    file_size = message.document.file_size if message.document else message.video.file_size

    # Save File to DB
    save_file(file_id, file_name, file_type, file_size, user_id)
    log_activity(user_id, "file_uploaded", file_id)

    # Send File Link
    await message.reply_text(f"✅ File Saved Successfully!

🔗 File ID: `{file_id}`", quote=True)

    # Auto Delete After Time
    await message.delete_in(FILE_AUTO_DELETE)
