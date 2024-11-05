import requests
import data
import data_requests

URL = data.URL

new_data = "Turkish Airlines"

res = requests.put(url=f"{URL}/channels/{data_requests.channel_1_id}", json={"name": new_data})
print("Response: ", res.status_code)
print("Data: ", res.json())
