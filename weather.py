import requests
import json

api_key = "9d0500XXXXXXXXXXXXXXX"
city = "London"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)

response = requests.get(url)
data = json.loads(response.text)
print(data)