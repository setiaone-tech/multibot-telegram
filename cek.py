import requests
from PIL import Image
from io import BytesIO

url = "http://lolhuman.herokuapp.com/api/onecak"
response = requests.get(url).content
if type(response) == bytes:
    with Image.open(BytesIO(response)) as im:
        im.save("cek/cek.png")