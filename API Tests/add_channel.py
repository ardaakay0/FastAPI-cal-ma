import requests
import data

URL = data.URL

res = requests.post(url=f"{URL}/channels/", json=data.channel_1)
print("Response: ", res.status_code)
res = requests.post(url=f"{URL}/channels/", json=data.channel_2)
print("Response: ", res.status_code)