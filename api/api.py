from io import BytesIO

import requests
from PIL import Image


brawlers_url = "https://api.brawlapi.com/v1/brawlers"
brawlers_data = requests.get(brawlers_url).json()['list']

for brawler_obj in brawlers_data:
    icon_url = brawler_obj['imageUrl2']
    response = requests.get(icon_url)
    image = Image.open(BytesIO(response.content))
    image.save(f"./assets/brawler_icons/{str(brawler_obj['name']).lower()}.png")
