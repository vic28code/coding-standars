"""Este módulo gestiona estudiantes y sus notas."""

class Student:
    """Clase para almacenar y procesar información del estudiante."""

    def __init__(s, id, name):
        s.id = id
        s.name = name
        s.gradez = []
        s.isPassed = "NO"
        s.honor = "?"

    def addGrades(self, g):
        self.gradez.append(g)

    def calcaverage(self):
        t = 0
        for x in self.gradez:
            t += x

        avg = t / len(self.gradez) if self.gradez else 0
        return avg

    def checkHonor(self):
        if self.calcaverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        print("Final Grade = " + self.letter)

def startrun():
    a = Student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)
    a.report()

startrun()
