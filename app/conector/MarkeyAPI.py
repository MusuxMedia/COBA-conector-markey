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
        r = self.__getRequest(dni)
        if r.status_code != 200:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token o Apikey de Markey Incorrecta")
        return r.json()

    def __getHeaders(self):
        return {
            'token': self.token,
            'Content-Type': 'application/json'
        }

    def __getPayloadM(self, dni):
        return json.dumps({
            "aplicacion": "MusuxMedia",
            "operacion": self.operacion,
            "apiKey": self.apikey,
            "filtro": {
                "persNroDocumento": dni,
                "persSexo" : "M",
                "ubicCodigo": 1
            }
        })

    def __getPayloadF(self, dni):
        return json.dumps({
            "aplicacion": "MusuxMedia",
            "operacion": self.operacion,
            "apiKey": self.apikey,
            "filtro": {
                "persNroDocumento": dni,
                "persSexo" : "F",
                "ubicCodigo": 1
            }
        })

    def __getRequest(self, dni):
        r = requests.request("GET", self.url, headers=self.__getHeaders(), data=self.__getPayloadM(dni))
        r1 = requests.request("GET", self.url, headers=self.__getHeaders(), data=self.__getPayloadF(dni))


        if r.status_code == 200:
            print("hola")
            return r
        else:
            return r1
