import requests
import data

URL = data.URL

res = requests.get(url=f"{URL}/salesreps/")
print("Response: ", res.status_code)
print("Data: ", res.json())