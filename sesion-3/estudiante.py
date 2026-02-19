import numpy as np

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = np.array(notas)

    def calculo(self):
        promedio = np.mean(self.notas)

        if promedio >= 11:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        return f"El estudiante {self.nombre} tiene un promedio de {promedio} y está {estado}."

alumno = Estudiante("Juan", [11, 13, 10, 9])
resultado = alumno.calculo()
print(resultado)