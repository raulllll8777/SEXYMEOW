import logging
import random
import asyncio
from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC import app

waifu_images = [
    "https://telegra.ph/file/fa707de344a816e1ec02a.mp4",
    "https://telegra.ph/file/c32910e1c2ecdf9887f96.mp4",
    "https://telegra.ph/file/b758e1413ce85fd14af5f.mp4",
    "https://telegra.ph/file/77a1dc50d0f5437d2b4f4.mp4",
    "https://telegra.ph/file/1f8ee0b5082f1b20b6a92.mp4",
    "https://telegra.ph/file/4ca6dae1497d7730f73e6.mp4",
    "https://telegra.ph/file/4ca6dae1497d7730f73e6.mp4",
    "https://telegra.ph/file/1f8ee0b5082f1b20b6a92.mp4",
    "https://telegra.ph/file/aa132aab086726e950fbc.mp4",
    "https://telegra.ph/file/76e188ec66031d25e06ca.mp4",
    "https://telegra.ph/file/76e188ec66031d25e06ca.mp4",
    "https://telegra.ph/file/ac46cefb2e56068f0a7cc.mp4",
    "https://telegra.ph/file/0b0851d7240b0cba7a1b2.mp4",
    "https://telegra.ph/file/18c9b0a8dcc226a61b828.mp4",
    "https://telegra.ph/file/1dd960a9ead0c9cfad6e8.mp4",
    "https://telegra.ph/file/62071514b3602fc20e52c.mp4",
    "https://telegra.ph/file/6851ca433d272d3345da8.mp4",
    "https://telegra.ph/file/5d8a04516496e00a4bc79.mp4",
    "https://telegra.ph/file/5d8a04516496e00a4bc79.mp4",
    "https://telegra.ph/file/5d8a04516496e00a4bc79.mp4",
    "https://telegra.ph/file/5d8a04516496e00a4bc79.mp4",
    "https://telegra.ph/file/5d8a04516496e00a4bc79.mp4",
    "https://telegra.ph/file/5d8a04516496e00a4bc79.mp4",
    "https://telegra.ph/file/5d8a04516496e00a4bc79.mp4",
    "https://telegra.ph/file/6851ca433d272d3345da8.mp4",
    "https://telegra.ph/file/62071514b3602fc20e52c.mp4",
    "https://telegra.ph/file/1dd960a9ead0c9cfad6e8.mp4",
    "https://telegra.ph/file/18c9b0a8dcc226a61b828.mp4",
    "https://telegra.ph/file/1dd960a9ead0c9cfad6e8.mp4",
    "https://telegra.ph/file/62071514b3602fc20e52c.mp4",
]

@app.on_message(filters.command("bro"))
async def es_img(_, message):
    image = random.choice(waifu_images)
    sent_message = await message.reply_video(video=image)

    await asyncio.sleep(99)

    await sent_message.delete()
