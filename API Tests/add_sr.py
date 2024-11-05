import requests
import data

URL = data.URL


res = requests.post(url=f"{URL}/salesreps/", json=data.sr_1)
print("Response: ", res.status_code)
res = requests.post(url=f"{URL}/salesreps/", json=data.sr_2)
print("Response: ", res.status_code)