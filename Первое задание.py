import json
import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
respons = requests.get(url)
data = json.loads(respons.text)
print(data)
