import requests
import data
import data_requests

URL = data.URL

new_data = "Arda A."

res = requests.put(url=f"{URL}/customers/{data_requests.customer_1_id}", json={"name": new_data})
print("Response: ", res.status_code)
print("Data: ", res.json())
