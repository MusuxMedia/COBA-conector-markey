from typing import Annotated

from fastapi import FastAPI, Depends

from app.conector import *

app = FastAPI()

def get_settings():
    return Settings()

@app.post("/markey")
async def request(data: RequestModel, credenciales: Annotated[Settings, Depends(get_settings)]):
    request = ProcessOrganizer(data.dni, credenciales)
    return request.validate_data()
