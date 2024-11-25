from fastapi import HTTPException, status


class DataValidator:
    def __init__(self, json_dict):
        self.data = json_dict

    def isValid(self):
        return len(self.data) > 0


    def getFirstname(self, paciente):
        try:
            return paciente["paciPaciente"]
        except KeyError:
            return ""

    def getLastname(self, paciente):
        try:
            return paciente["paciPaciente"]
        except KeyError:
            return ""

    def getMotivo(self, paciente):
        try:
            return paciente["turnEfector"]
        except KeyError:
            return ""
