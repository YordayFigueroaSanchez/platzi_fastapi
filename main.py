import zoneinfo
from fastapi import FastAPI
from datetime import datetime

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


if __name__ == "__main__":
    main()


