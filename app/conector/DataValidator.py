from fastapi import HTTPException, status


class DataValidator:
    def __init__(self, json_dict):
        self.data = json_dict

    def isValid(self):
        return len(self.data) > 0


    def getFirstname(self):
        try:
            name = self.data[0]['paciPaciente'].split()
            return name[-1]
        except KeyError:
            return ""

    def getLastname(self):
        try:
            name = self.data[0]['paciPaciente'].split()
            return " ".join(name[0:-1])
        except KeyError:
            return ""

    def getFecha(self, app):
        try:
            return app["turnFechaInicio"]
        except KeyError:
            return ""

    def getAppointments(self):
        diccio = dict()
        l = []
        for appointment in self.data:
            l.append({
                "queue.name" : "Con turno",
                "url" : "/api/terminal/queueUp",
                "startAt": self.getFecha(appointment)
            })
        diccio["buttons"] = l
        return diccio
