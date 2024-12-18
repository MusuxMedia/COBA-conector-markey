from fastapi import HTTPException, status


class DataValidator:
    def __init__(self, json_dict):
        self.data = json_dict

    def isValid(self):
        return len(self.data) > 0


    def getFirstname(self, appointment):
        try:
            name = appointment['paciPaciente'].split()
            return name[-1]
        except KeyError:
            return ""

    def getLastname(self, appointment):
        try:
            name = appointment['paciPaciente'].split()
            return " ".join(name[0:-1])
        except KeyError:
            return ""

    def getFecha(self, appointment):
        try:
            return appointment["turnFechaInicio"]
        except KeyError:
            return ""

