from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MARKEY_URL: str = "https://coba.markey.com.ar/APIMarkeyV2/obtener"
    MARKEY_TOKEN: str = '9b94d8c8-e6b6-447a-91c5-62e377ba17b3'
    MARKEY_API_KEY: str = "b473552d-cbe8-42c2-8de9-c8aad68bf6e0"
    CUSTOMERTYPE: str = "829"
    NO_CUSTOMERTYPE: str = "799"
    OPERATION: str = "obtenerTurnosPaciente"
