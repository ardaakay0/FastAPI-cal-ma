import requests
import data
import data_requests

URL = data.URL

new_data = 1000

res = requests.put(url=f"{URL}/routes/{data_requests.route_1_id}", json={"distance_travelled": new_data})
print("Response: ", res.status_code)
print("Data: ", res.json())
