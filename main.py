from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from starlette.responses import FileResponse
from datetime import datetime
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Add these lines after creating the FastAPI app
@app.get("/", include_in_schema=False)
async def read_index():
    return FileResponse('index.html')

@app.get("/database.html", include_in_schema=False)
async def read_database():
    return FileResponse('database.html')

class Address(BaseModel):
    street: str
    apt_no: int
    neighbourhood: str
    district: str
    city: str
    address_id: UUID = None
    flat_no: int

class Channel(BaseModel):
    name: str
    service_time: float # datetime?
    channel_id: UUID = None
    visit_schedule: List[str] # Emin degilim
    visit_frequency: int

class Customer(BaseModel):
    name: str
    customer_id: UUID = None
    address: Address
    channel: Channel

class SalesRepresentative(BaseModel):
    name: str
    workload: int # Emin degilim
    sales_id: UUID = None
    time_window: List[str] # Fixed typo from time_tindow

class Route(BaseModel):
    route_id: UUID = None
    time_spend: float
    distance_travelled: float
    start_time: datetime
    end_time: datetime
    customer: Customer

# Buralar SQL ile degistirilecek
addresses = []
channels = []
customers = []
salesrepresentatives = []
routes = []

# Add these helper functions at the top of the file, after the model definitions
def is_duplicate_address(new_address: Address) -> bool:
    return any(
        addr.street == new_address.street and
        addr.apt_no == new_address.apt_no and
        addr.flat_no == new_address.flat_no and
        addr.neighbourhood == new_address.neighbourhood and
        addr.district == new_address.district and
        addr.city == new_address.city
        for addr in addresses
    )

def is_duplicate_channel(new_channel: Channel) -> bool:
    return any(
        ch.name == new_channel.name and
        ch.service_time == new_channel.service_time and
        ch.visit_frequency == new_channel.visit_frequency and
        ch.visit_schedule == new_channel.visit_schedule
        for ch in channels
    )

def is_duplicate_customer(new_customer: Customer) -> bool:
    return any(
        cust.name == new_customer.name and
        cust.address.dict(exclude={'address_id'}) == new_customer.address.dict(exclude={'address_id'}) and
        cust.channel.dict(exclude={'channel_id'}) == new_customer.channel.dict(exclude={'channel_id'})
        for cust in customers
    )

def is_duplicate_salesrep(new_salesrep: SalesRepresentative) -> bool:
    return any(
        sr.name == new_salesrep.name and
        sr.workload == new_salesrep.workload and
        sr.time_window == new_salesrep.time_window
        for sr in salesrepresentatives
    )

def is_duplicate_route(new_route: Route) -> bool:
    return any(
        r.time_spend == new_route.time_spend and
        r.distance_travelled == new_route.distance_travelled and
        r.start_time == new_route.start_time and
        r.end_time == new_route.end_time and
        r.customer.dict(exclude={'customer_id'}) == new_route.customer.dict(exclude={'customer_id'})
        for r in routes
    )

# Add address to list
@app.post("/addresses/", response_model=Address)
def create_address(address: Address):
    if is_duplicate_address(address):
        raise HTTPException(
            status_code=400,
            detail="An address with these details already exists"
        )
    address.address_id = uuid4()
    addresses.append(address)
    return address

# Get all addresses
@app.get("/addresses/", response_model=List[Address])
def read_addresses():
    return addresses

# Get address by ID. Raise exception if address id doesn't exist
@app.get("/addresses/{address_id}", response_model=Address)
def read_address(address_id: UUID):
    for address in addresses:
        if address.address_id == address_id:
            return address
    raise HTTPException(status_code=404, detail="Address not found")

# Update address's elements by using address_id. Raise exception if address id doesn't exist
@app.put("/addresses/{address_id}", response_model=Address)
def update_address(address_id: UUID, address_update: Address):
    for ind, address in enumerate(addresses):
        if address.address_id == address_id:
            updated_address = address.copy(update=address_update.dict(exclude_unset=True))
            addresses[ind] = updated_address
            return updated_address
    raise HTTPException(status_code=404, detail="Address not found")

# Delete address from the list by using address_id. Raise exception if address id doesn't exist
@app.delete("/addresses/{address_id}", response_model = Address)
def delete_address(address_id: UUID):
    for ind, address in enumerate(addresses):
        if address.address_id == address_id:
            return addresses.pop(ind)
    raise HTTPException(status_code = 404, detail="Address not found")

# Clears the list
@app.put("/addresses/delete_all/", response_model=List[Address])
def clear_list():
    global addresses
    addresses.clear()
    return addresses

# Add all the new endpoints for Channel
@app.post("/channels/", response_model=Channel)
def create_channel(channel: Channel):
    if is_duplicate_channel(channel):
        raise HTTPException(
            status_code=400,
            detail="A channel with these details already exists"
        )
    channel.channel_id = uuid4()
    channels.append(channel)
    return channel

@app.get("/channels/", response_model=List[Channel])
def read_channels():
    return channels

@app.get("/channels/{channel_id}", response_model=Channel)
def read_channel(channel_id: UUID):
    for channel in channels:
        if channel.channel_id == channel_id:
            return channel
    raise HTTPException(status_code=404, detail="Channel not found")

@app.put("/channels/{channel_id}", response_model=Channel)
def update_channel(channel_id: UUID, channel_update: Channel):
    for ind, channel in enumerate(channels):
        if channel.channel_id == channel_id:
            updated_channel = channel.copy(update=channel_update.dict(exclude_unset=True))
            channels[ind] = updated_channel
            return updated_channel
    raise HTTPException(status_code=404, detail="Channel not found")

@app.delete("/channels/{channel_id}", response_model=Channel)
def delete_channel(channel_id: UUID):
    for ind, channel in enumerate(channels):
        if channel.channel_id == channel_id:
            return channels.pop(ind)
    raise HTTPException(status_code=404, detail="Channel not found")

@app.put("/channels/delete_all/", response_model=List[Channel])
def clear_channels():
    global channels
    channels.clear()
    return channels

# Add all the new endpoints for Customer
@app.post("/customers/", response_model=Customer)
def create_customer(customer: Customer):
    if is_duplicate_customer(customer):
        raise HTTPException(
            status_code=400,
            detail="A customer with these details already exists"
        )
    customer.customer_id = uuid4()
    customers.append(customer)
    return customer

@app.get("/customers/", response_model=List[Customer])
def read_customers():
    return customers

@app.get("/customers/{customer_id}", response_model=Customer)
def read_customer(customer_id: UUID):
    for customer in customers:
        if customer.customer_id == customer_id:
            return customer
    raise HTTPException(status_code=404, detail="Customer not found")

@app.put("/customers/{customer_id}", response_model=Customer)
def update_customer(customer_id: UUID, customer_update: Customer):
    for ind, customer in enumerate(customers):
        if customer.customer_id == customer_id:
            updated_customer = customer.copy(update=customer_update.dict(exclude_unset=True))
            customers[ind] = updated_customer
            return updated_customer
    raise HTTPException(status_code=404, detail="Customer not found")

@app.delete("/customers/{customer_id}", response_model=Customer)
def delete_customer(customer_id: UUID):
    for ind, customer in enumerate(customers):
        if customer.customer_id == customer_id:
            return customers.pop(ind)
    raise HTTPException(status_code=404, detail="Customer not found")

@app.put("/customers/delete_all/", response_model=List[Customer])
def clear_customers():
    global customers
    customers.clear()
    return customers

# Add all the new endpoints for SalesRepresentative
@app.post("/salesreps/", response_model=SalesRepresentative)
def create_salesrep(salesrep: SalesRepresentative):
    if is_duplicate_salesrep(salesrep):
        raise HTTPException(
            status_code=400,
            detail="A sales representative with these details already exists"
        )
    salesrep.sales_id = uuid4()
    salesrepresentatives.append(salesrep)
    return salesrep

@app.get("/salesreps/", response_model=List[SalesRepresentative])
def read_salesreps():
    return salesrepresentatives

@app.get("/salesreps/{sales_id}", response_model=SalesRepresentative)
def read_salesrep(sales_id: UUID):
    for salesrep in salesrepresentatives:
        if salesrep.sales_id == sales_id:
            return salesrep
    raise HTTPException(status_code=404, detail="Sales Representative not found")

@app.put("/salesreps/{sales_id}", response_model=SalesRepresentative)
def update_salesrep(sales_id: UUID, salesrep_update: SalesRepresentative):
    for ind, salesrep in enumerate(salesrepresentatives):
        if salesrep.sales_id == sales_id:
            updated_salesrep = salesrep.copy(update=salesrep_update.dict(exclude_unset=True))
            salesrepresentatives[ind] = updated_salesrep
            return updated_salesrep
    raise HTTPException(status_code=404, detail="Sales Representative not found")

@app.delete("/salesreps/{sales_id}", response_model=SalesRepresentative)
def delete_salesrep(sales_id: UUID):
    for ind, salesrep in enumerate(salesrepresentatives):
        if salesrep.sales_id == sales_id:
            return salesrepresentatives.pop(ind)
    raise HTTPException(status_code=404, detail="Sales Representative not found")

@app.put("/salesreps/delete_all/", response_model=List[SalesRepresentative])
def clear_salesreps():
    global salesrepresentatives
    salesrepresentatives.clear()
    return salesrepresentatives

# Add all the new endpoints for Route
@app.post("/routes/", response_model=Route)
def create_route(route: Route):
    if is_duplicate_route(route):
        raise HTTPException(
            status_code=400,
            detail="A route with these details already exists"
        )
    route.route_id = uuid4()
    routes.append(route)
    return route

@app.get("/routes/", response_model=List[Route])
def read_routes():
    return routes

@app.get("/routes/{route_id}", response_model=Route)
def read_route(route_id: UUID):
    for route in routes:
        if route.route_id == route_id:
            return route
    raise HTTPException(status_code=404, detail="Route not found")

@app.put("/routes/{route_id}", response_model=Route)
def update_route(route_id: UUID, route_update: Route):
    for ind, route in enumerate(routes):
        if route.route_id == route_id:
            updated_route = route.copy(update=route_update.dict(exclude_unset=True))
            routes[ind] = updated_route
            return updated_route
    raise HTTPException(status_code=404, detail="Route not found")

@app.delete("/routes/{route_id}", response_model=Route)
def delete_route(route_id: UUID):
    for ind, route in enumerate(routes):
        if route.route_id == route_id:
            return routes.pop(ind)
    raise HTTPException(status_code=404, detail="Route not found")

@app.put("/routes/delete_all/", response_model=List[Route])
def clear_routes():
    global routes
    routes.clear()
    return routes

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5500)