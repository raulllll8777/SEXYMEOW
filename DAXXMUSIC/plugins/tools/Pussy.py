import requests
import random 
from requests import get
from bs4 import BeautifulSoup
from DAXXMUSIC import app
from pyrogram import filters
from pyrogram.types import InputMediaPhoto

def get_image_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    image_tags = soup.find_all('img')
    image_urls = [img['src'] for img in image_tags if 'src' in img.attrs]

    return image_urls
  
@app.on_message(filters.command("chod"))
def ncosplay_pyrogram(client, message):
    website_url = "https://ososedki.com/cosplays"

    image_urls = get_image_urls(website_url)

    if image_urls:
        random_image_url = random.choice(image_urls)

        client.send_photo(message.chat.id, photo=random_image_url)
    else:
        message.reply_text("No images found.")
