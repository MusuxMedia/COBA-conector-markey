class Paciente(dict):
    def __init__(self, nombre, apellido, dni):
        dict.__init__(self)
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __repr__(self):
        return self.toJson()

    def toJson(self):
        return {
            "firstName": self.nombre,
            "lastName": self.apellido,
            "dni": self.dni,
            "extraFields":
                {

                }
        }
