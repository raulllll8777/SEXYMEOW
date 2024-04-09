import re
from dotenv import load_dotenv
from pyrogram import filters
import random
from pyrogram.types import Message
from pyrogram import Client, filters
from DAXXMUSIC import app



# "/gm" command ka handler
@app.on_message(filters.command("goodmorning", prefixes="g"))
def goodnight_command_handler(client: Client, message: Message):
    # Randomly decide whether to send a sticker or an emoji
    send_sticker = random.choice([True, False])
    
    # Send a sticker or an emoji based on the random choice
    if send_sticker:
        client.send_sticker(message.chat.id, get_random_sticker())
    else:
        client.send_message(message.chat.id, get_random_emoji())

# Function to get a random sticker
def get_random_sticker():
    stickers = [
        "CAACAgUAAx0CcdFlwAABJEwtZhUtGNmL1wI9s-0LAt1y603baCcAAgcQAAJpOqlUOX594IPS_TYeBA",
        "CAACAgUAAx0CcdFlwAABJEwtZhUtGNmL1wI9s-0LAt1y603baCcAAgcQAAJpOqlUOX594IPS_TYeBA",
        "CAACAgUAAx0CcdFlwAABJEwtZhUtGNmL1wI9s-0LAt1y603baCcAAgcQAAJpOqlUOX594IPS_TYeBA",
        "CAACAgUAAx0CcdFlwAABJEwtZhUtGNmL1wI9s-0LAt1y603baCcAAgcQAAJpOqlUOX594IPS_TYeBA",
        "CAACAgUAAx0CcdFlwAABJEwtZhUtGNmL1wI9s-0LAt1y603baCcAAgcQAAJpOqlUOX594IPS_TYeBA",
    ]
    return random.choice(stickers)

# Function to get a random emoji
def get_random_emoji():
    emojis = [
        "🌤",
        "🌤", 
        "🌞",
        
    ]
    return random.choice(emojis)
