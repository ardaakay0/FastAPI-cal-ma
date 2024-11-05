import requests
import data
import data_requests

URL = data.URL

res = requests.get(url=f"{URL}/addresses/{data_requests.address_1_id}")
print("Response: ", res.status_code)
print("Data: ", res.json())
