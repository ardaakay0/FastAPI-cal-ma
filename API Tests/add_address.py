import requests
import data

URL = data.URL

res = requests.post(url=f"{URL}/addresses/", json=data.address_1)
print("Response: ", res.status_code)
res = requests.post(url=f"{URL}/addresses/", json=data.address_2)
print("Response: ", res.status_code)