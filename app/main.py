import zoneinfo
from datetime import datetime
import time
from db import create_all_tables
from .routers import customers, transactions, invoices, plans
from fastapi import FastAPI, Request, Depends 
from fastapi.security import HTTPBasic, HTTPBasicCredentials 
from typing import Annotated
from fastapi.exceptions import HTTPException
from fastapi import status

app = FastAPI(lifespan=create_all_tables)

app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(invoices.router)
app.include_router(plans.router)

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"{request.method} {request.url} {response.status_code} {process_time}")
    return response

security = HTTPBasic()

@app.get("/")
async def read_root(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    print(credentials)
    if credentials.username == "admin" and credentials.password == "admin":
        return {"message": f"Hello {credentials.username} !!!"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

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
async def get_time_by_iso_code(iso_code: str):
    iso = iso_code.upper()
    timezone = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone)
    return {"time": datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")}





if __name__ == "__main__":
    main()


