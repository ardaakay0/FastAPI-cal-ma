import requests
import data

URL = data.URL

res = requests.post(url=f"{URL}/customers/", json=data.customer_1)
print("Response: ", res.status_code)
res = requests.post(url=f"{URL}/customers/", json=data.customer_2)
print("Response: ", res.status_code)