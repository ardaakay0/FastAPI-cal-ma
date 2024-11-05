import requests
import data

URL = data.URL

res = requests.put(url=f"{URL}/customers/delete_all/")
print("Response: ", res.status_code)
