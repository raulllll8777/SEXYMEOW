from pyrogram import Client, filters
import requests
import random
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  
from DAXXMUSIC import app

async def delete_message_after_timeout(message, timeout):
    await asyncio.sleep(timeout)
    await message.delete()

regex_photo = ["waifu"]
pht = random.choice(regex_photo)
url = f"https://api.waifu.pics/nsfw/{pht}"

@app.on_message(filters.command("nwaifu"))
async def get_waifu(client, message):
    response = requests.get(url).json()
    up = response.get('url')

    if up:
        button = [[InlineKeyboardButton("SUPPORT", url="https://t.me/naruto_support1")]]
        markup = InlineKeyboardMarkup(button)
        
        sent_message = await message.reply_photo(up, caption="BY @ushio_kofun_bot ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ɪɴ 30 ꜱᴇᴄᴏɴᴅ", reply_markup=markup)
        
        # Delete the sent message after 1 minute
        asyncio.create_task(delete_message_after_timeout(sent_message, 30))
    else:
        await message.reply("Request failed, try /again")
