import requests
import data
import data_requests

URL = data.URL

res = requests.delete(url=f"{URL}/customers/{data_requests.customer_1_id}/")
print("Response: ", res.status_code)