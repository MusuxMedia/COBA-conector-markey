from fastapi import HTTPException
from starlette.responses import JSONResponse

from . import DataValidator
from . import MarkeyAPI



class ProcessOrganizer:
    def __init__(self, dni: str, credenciales):
        self.dni = dni
        self.credenciales = credenciales

    def validate_data(self):
        markey_response = MarkeyAPI(self.credenciales).getResponse(self.dni)
        validator: DataValidator = DataValidator(markey_response)
        if validator.isValid():
            return self.build_response(validator)
        else:
            return JSONResponse(
                status_code=404,
                content={"key": "noAppointmentsMatch"}
            )

    def build_response(self, validator: DataValidator):
        l = []
        for app in validator.data:
            l.append(
                {
                    "firstName": validator.getFirstname(app),
                    "lastName": validator.getLastname(app),
                    "dni": self.dni,
                    "queue": {
                        "name": "Con turno"
                    },
                    "queueName" : "Turno programado",
                    "startAt": validator.getFecha(app),
                    "endAt": validator.getFecha(app)
                }
            )
        return l
