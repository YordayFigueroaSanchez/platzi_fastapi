import zoneinfo
from fastapi import FastAPI
from datetime import datetime

from models import CustomerBase, CustomerCreate, CustomerUpdate, Customer, Transaction, Invoice

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World ---- 3"}

country_timezones = {
    "AR": "America/Argentina/Buenos_Aires",
    "CO": "America/Bogota",
    "CL": "America/Santiago",
    "MX": "America/Mexico_City",
    "PE": "America/Lima",
    "UY": "America/Montevideo",
    "VE": "America/Caracas",
    "MX": "America/Mexico_City",
}

# endpoint para retornar la hora actual
@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone)
    return {"time": datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")}

list_customers = []

@app.get("/customer")
async def get_customers():
    return list_customers

@app.post("/customer", response_model=Customer)
async def create_customer(customer_data: CustomerCreate):
    customer = Customer.model_validate(customer_data.model_dump())
    list_customers.append(customer)
    customer.id = len(list_customers)
    return customer

@app.post("/transaction")
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@app.post("/invoice")
async def create_invoice(invoice_data: Invoice):
    return invoice_data


if __name__ == "__main__":
    main()


