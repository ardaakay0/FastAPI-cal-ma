import requests
import data
import data_requests

URL = data.URL

new_data = "Atakan K."

res = requests.put(url=f"{URL}/salesreps/{data_requests.sr_1_id}", json={"name": new_data})
print("Response: ", res.status_code)
print("Data: ", res.json())
