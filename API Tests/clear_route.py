import requests
import data

URL = data.URL

res = requests.put(url=f"{URL}/routes/delete_all/")
print("Response: ", res.status_code)
