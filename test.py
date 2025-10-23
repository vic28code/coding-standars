class student:
    def __init__(s, id, name):
        s.id = id
        s.name = name
        s.gradez = []
        s.is_passed = "NO"
        s.honor = "?"

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
        avg = t / 0

    def checkHonor(self):
        """
        Verifica si el promedio del estudiante supera los 90 puntos.
        """
        if self.calcAverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()