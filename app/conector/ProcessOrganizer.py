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
            return self.build_paciente(validator)
        else:
            return []

    def build_paciente(self, validator: DataValidator):
        return Paciente(nombre=validator.getFirstname(self))

