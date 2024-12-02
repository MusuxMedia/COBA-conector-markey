import json

from . import MarkeyAPI
from . import DataValidator
from . import Paciente
from .config import Settings


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
            return []

    def build_response(self, validator: DataValidator):
        return [{
            "firstName": validator.getFirstname(),
            "lastName": validator.getLastname(),
            "dni": self.dni,
            "selectionName" : validator.getLastname(),
            "customerType": {
                "id": Settings().CUSTOMERTYPE
            },
            "appointment": validator.getAppointments(),
        }]
