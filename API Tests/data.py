URL = "http://0.0.0.0:5500"

address_1 = {
    "street": "Özyeğin Üniversitesi",
    "apt_no": 43,
    "neighbourhood": "Nişantepe",
    "district": "Çekmeköy",
    "city": "İstanbul",
    "flat_no": 12
}

address_2 = {
    "street": "1000 5th Ave",
    "apt_no": 102,
    "neighbourhood": "Williamsburg",
    "district": "Brooklyn",
    "city": "New York",
    "flat_no": 24
}

channel_1 = {
    "name": "Channel 1",
    "service_time": 10,
    "visit_schedule": ["Monday", "Wednesday", "Friday"],
    "visit_frequency": 3
}

channel_2 = {
    "name": "Channel 2",
    "service_time": 15,
    "visit_schedule": ["Tuesday", "Thursday", "Saturday"],
    "visit_frequency": 2
}

customer_1 = {
    "name": "Customer 1",
    "address": address_1,
    "channel": channel_1
}

customer_2 = {
    "name": "Customer 2",
    "address": address_2,
    "channel": channel_2
}

sr_1 = {
    "name": "Sales Representative 1",
    "workload": 10,
    "time_window": ["Monday", "Wednesday", "Friday"]
}

sr_2 = {
    "name": "Sales Representative 2",
    "workload": 15,
    "time_window": ["Tuesday", "Thursday", "Saturday"]
}

route_1 = {
    "time_spend": 23,
    "distance_travelled": 130,
    "start_time": "2024-01-01 10:00:00",
    "end_time": "2024-01-01 10:10:00",
    "customer": customer_1
}

route_2 = {
    "time_spend": 18,
    "distance_travelled": 100,
    "start_time": "2024-01-01 12:12:00",
    "end_time": "2024-01-01 12:22:00",
    "customer": customer_2
}