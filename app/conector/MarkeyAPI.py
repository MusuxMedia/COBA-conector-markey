import json
import requests
from fastapi import status, HTTPException


class MarkeyAPI:
    def __init__(self, credenciales):
        self.url = credenciales.MARKEY_URL
        self.token = credenciales.MARKEY_TOKEN
        self.apikey = credenciales.MARKEY_API_KEY
        self.operacion = credenciales.OPERATION

    def getResponse(self, dni):
        # Agrego dos DNIs de prueba
        if dni == "44553142":
            return [{
                "paciPaciente": "Valentin Pugliese",
                "turnFechaInicio": "2022-03-29T15:00:00-0300"
            }]
        if dni == "32438618":
            return [{
                "paciPaciente": "Sonia Neibirt",
                "turnFechaInicio": "2024-05-25T15:00:00-0300"
            }]
        r = requests.request("GET", self.url, headers=self.__getHeaders(), data=self.__getPayload(dni))
        if r.status_code != 200:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token o Apikey de Markey Incorrecta")
        return r.json()

    def __getHeaders(self):
        return {
            'token': self.token,
            'Content-Type': 'application/json'
        }

    def __getPayload(self, dni):
        return json.dumps({
            "aplicacion": "MusuxMedia",
            "operacion": self.operacion,
            "apiKey": self.apikey,
            "filtro": {
                "persNroDocumento": dni
            }
        })
