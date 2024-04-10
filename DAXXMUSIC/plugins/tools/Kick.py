from pyrogram import Client, filters
import requests
import random
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  
from DAXXMUSIC import app

regex_gif = ["kick"]
pht = random.choice(regex_gif)
url = f"https://api.waifu.pics/sfw/kick}"

@app.on_message(filters.command("kick"))
def get_waifu(client, message):
    response = requests.get(url).json()
    up = response['url']
    if up:
        message.reply_video(up,caption="BY @ushio_kofun_bot)
    else:
        message.reply("Request failed try /again")
