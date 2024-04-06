import requests
import asyncio
from pyrogram import filters
from pyrogram.types import Message
import time
from DAXXMUSIC import app

async def delete_message_after_timeout(message, timeout):
    await asyncio.sleep(timeout)
    await message.delete()

@app.on_message(filters.command("nudes"))
async def es_img(_, message):
    url = "http://api.nekos.fun:8080/api/4k"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        data = response.json()
        image = data.get("image")

        if image:
            sent_message = await message.reply_photo(image, caption="ʙʏ @ushio_kofun_bot", parse_mode=None)
            asyncio.create_task(delete_message_after_timeout(sent_message, 30))  # Delete after 1 minute
        else:
            await message.reply_text("No image found.")
    except requests.RequestException as e:
        # Handle request-related errors
        await message.reply_text(f"Error: {str(e)}")
    except Exception as e:
        # Handle other unexpected errors
        await message.reply_text(f"Unexpected error: {str(e)}")
