import requests
import data

URL = data.URL

res = requests.get(url=f"{URL}/addresses/")
data = res.json()
address_1_id = data[0]["address_id"]
address_2_id = data[1]["address_id"]

res = requests.get(url=f"{URL}/channels/")
data = res.json()
channel_1_id = data[0]["channel_id"]
channel_2_id = data[1]["channel_id"]

res = requests.get(url=f"{URL}/customers/")
data = res.json()
customer_1_id = data[0]["customer_id"]
customer_2_id = data[1]["customer_id"]

res = requests.get(url=f"{URL}/routes/")
data = res.json()
route_1_id = data[0]["route_id"]
route_2_id = data[1]["route_id"]

res = requests.get(url=f"{URL}/salesreps/")
data = res.json()
sr_1_id = data[0]["sales_id"]
sr_2_id = data[1]["sales_id"]
