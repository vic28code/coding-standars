"""Este módulo gestiona estudiantes y sus notas."""


class Student:

    """Clase para almacenar y procesar información del estudiante."""

    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.gradez = []
        self.is_passed = "NO"
        self.honor = "?"
        self.letter = None

    def add_grades(self, g):
        """
        Agrega una nueva nota/calificación a la lista de notas del estudiante
        :param g: La nota a añadir.
        """
        self.gradez.append(g)

    def calcaverage(self):
        """
        Calcula y devuelve el promedio de las notas (gradez) del estudiante.

        :returns: El promedio de las notas o 0 si no hay notas.
        :rtype: float
        """
        t = 0
        for x in self.gradez:
            t += x
        avg = t / len(self.gradez) if self.gradez else 0
        self.letter = avg
        return avg

    def check_honor(self):
        """
        Verifica si el promedio del estudiante supera los 90 puntos.
        """
        if self.calcaverage() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """
        Elimina la nota del estudiante.
        """
        del self.gradez[index]

    def report(self):  # broken format
        """
        Imprime un resumen del estudiante (ID, nombre, conteo y nota final)
        """
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        print("Final Grade = " + self.letter)


def startrun():
    """Función de arranque que ejecuta un ejemplo mínimo"""
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")
    a.calcaverage()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
