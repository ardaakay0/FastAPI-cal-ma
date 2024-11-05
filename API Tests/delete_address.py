import requests
import data
import data_requests

URL = data.URL

res = requests.delete(url=f"{URL}/addresses/{data_requests.address_1_id}/")
print("Response: ", res.status_code)