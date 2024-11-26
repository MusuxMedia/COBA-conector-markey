from fastapi import HTTPException, status


class DataValidator:
    def __init__(self, json_dict):
        self.data = json_dict

    def isValid(self):
        return len(self.data) > 0


    def getFirstname(self):
        try:
            return self.data[0]['paciPaciente']
        except KeyError:
            return ""

    def getLastname(self):
        try:
            return self.data[0]['paciPaciente']
        except KeyError:
            return ""

    def getMotivo(self):
        try:
            return self.data["turnEfector"]
        except KeyError:
            return ""
