import requests
import data
import data_requests

URL = data.URL

res = requests.get(url=f"{URL}/routes/{data_requests.route_1_id}")
print("Response: ", res.status_code)
print("Data: ", res.json())
