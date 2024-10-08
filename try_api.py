import requests
from pprint import pprint

base_url = "http://0.0.0.0:8000/tasks/"



task1 = {
    "title": "Do homework",
    "completed": "False"
}
task2 = {
    "title": "Practice Spanish",
    "description": "Me gustas tu",
    "completed": "False"
}
task3 = {
    "title": "Hangout with friends",
    "completed": "True"
}

# Delete all tasks from DB
""" res = requests.put(url=f"{base_url}delete_all/")
print(res.text) """

# Place tasks to DB
""" res = requests.post(url=base_url, json= task1)
print(f"[Task 1 POST] Status Code: {res.status_code}, Json: {res.json}\n")
res = requests.post(url=base_url, json=task2)
print(f"[Task 2 POST] Status Code: {res.status_code}, Json: {res.json}\n")
res = requests.post(url=base_url, json=task3)
print(f"[Task 3 POST] Status Code: {res.status_code}, Json: {res.json}\n") """

# Get all tasks from DB
res = requests.get(url=base_url)
print(f"[All Tasks GET] Tasks: {res.text}\n")
task1_id = res.json()[0]["id"]
task2_id = res.json()[1]["id"]
task3_id = res.json()[2]["id"]

# Get a specific task by using Task ID
res = requests.get(url=f"{base_url}{task1_id}")
print("[Task 1]")
pprint(res.json())
res = requests.get(url=f"{base_url}{task2_id}")
print("[Task 2]")
pprint(res.json())
res = requests.get(url=f"{base_url}{task3_id}")
print("[Task 3]")
pprint(res.json())

# Update a task by using Task ID
""" task2 = {
    "title": "Practice guitar",
    "completed": False
}
res = requests.put(url=f"{base_url}{task2_id}", json=task2)
pprint(res.json()) """

# Delete a task by using Task ID
res = requests.delete(url=f"{base_url}{task2_id}")
print(res.status_code)

# Show the DB one last time
res = requests.get(url=base_url)
pprint(res.json())