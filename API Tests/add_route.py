import requests
import data

URL = data.URL

res = requests.post(url=f"{URL}/routes/", json=data.route_1)
print("Response: ", res.status_code)
res = requests.post(url=f"{URL}/routes/", json=data.route_2)
print("Response: ", res.status_code)