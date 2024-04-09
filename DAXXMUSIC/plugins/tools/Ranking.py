from pyrogram import filters
from pymongo import MongoClient
from DAXXMUSIC import app
from config import MONGO_DB_URI
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random

mongo_client = MongoClient(MONGO_DB_URI)
db = mongo_client["natu_rankings"]
collection = db["ranking"]

user_data = {}
today = {}

ARU = [
    "https://graph.org/file/3a0066c6e12a4412b832c.jpg",
    "https://graph.org/file/3a0066c6e12a4412b832c.jpg",
    "https://graph.org/file/7d9eaee9efe95444fb5e3.jpg",
    "https://telegra.ph/file/f71f13dc4755349c13a70.jpg",
    "https://telegra.ph/file/0b99d9768000b9fbc7a28.jpg",
    "https://telegra.ph/file/6af06601caadb0e88e8fe.jpg",
    "https://telegra.ph/file/0cd3fdfb1c37e35860167.jpg",
    "https://telegra.ph/file/0cd3fdfb1c37e35860167.jpg",
    "https://graph.org/file/a45b214adabcd86401152.jpg",
]


@app.on_message(filters.group & filters.group, group=6)
def today_watcher(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_id in today and user_id in today[chat_id]:
        today[chat_id][user_id]["total_messages"] += 1
    else:
        if chat_id not in today:
            today[chat_id] = {}
        today[chat_id].setdefault(user_id, {"total_messages": 1})

@app.on_message(filters.group & filters.group, group=11)
def _watcher(_, message):
    if message.from_user:
        user_id = message.from_user.id    
        user_data.setdefault(user_id, {}).setdefault("total_messages", 0)
        user_data[user_id]["total_messages"] += 1    
        collection.update_one({"_id": user_id}, {"$inc": {"total_messages": 1}}, upsert=True)


@app.on_message(filters.command("today"))
async def today_(_, message):
    chat_id = message.chat.id
    if chat_id in today:
        users_data = [(user_id, user_data["total_messages"]) for user_id, user_data in today[chat_id].items()]
        sorted_users_data = sorted(users_data, key=lambda x: x[1], reverse=True)[:10]

        if sorted_users_data:
            response = "✦ 📈 ᴛᴏᴅᴀʏ's ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ**\n\n"
            for idx, (user_id, total_messages) in enumerate(sorted_users_data, start=1):
                try:
                    user_name = (await app.get_users(user_id)).first_name
                except:
                    user_name = "Unknown"
                user_info = f"{idx}.   {user_name} ➠ {total_messages}\n"
                response += user_info
            button = InlineKeyboardMarkup(
                [[    
                   InlineKeyboardButton("ᴏᴠᴇʀᴀʟʟ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ", callback_data="overall"),
                ]])
            await message.reply_photo(random.choice(ARU), caption=response, reply_markup=button)
        else:
            await message.reply_text("❅ ɴᴏ ᴅᴀᴛᴀ ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛᴏᴅᴀʏ.")
    else:
        await message.reply_text("❅ ɴᴏ ᴅᴀᴛᴀ ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛᴏᴅᴀʏ.")


@app.on_message(filters.command("ranking"))
async def ranking(_, message):
    top_members = collection.find().sort("total_messages", -1).limit(10)

    response = "✦ 📈 ᴏᴠᴇʀᴀʟʟ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ\n\n"
    for idx, member in enumerate(top_members, start=1):
        user_id = member["_id"]
        total_messages = member["total_messages"]
        try:
            user_name = (await app.get_users(user_id)).first_name
        except:
            user_name = "Unknown"

        user_info = f"{idx}.   {user_name} ➠ {total_messages}\n"
        response += user_info

    random_image = random.choice(ARU)  
    await message.reply_photo(photo=random_image, caption=response)
