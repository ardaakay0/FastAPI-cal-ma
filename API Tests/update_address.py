import requests
import data
import data_requests

URL = data.URL

new_data = "New Street"

res = requests.put(url=f"{URL}/addresses/{data_requests.address_1_id}", json={"street": new_data})
print("Response: ", res.status_code)
print("Data: ", res.json())
