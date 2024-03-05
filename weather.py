import requests
import json
from PIL import Image, ImageFont, ImageDraw 

api_key = "9d0500XXXXXXXXXXXXXXX"

city = "London"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)

response = requests.get(url)
data = json.loads(response.text)
print(data)

image = Image.open("post.png")
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('Inter.ttf', size=50)
content = "Latest Weather Forecast"
color = 'rgb(255, 255, 255)'
(x, y) = (55,50)
draw.text((x, y), content, color, font=font)

image.save("test.png")