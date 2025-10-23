class student:
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
        avg = t / 0

    def check_honor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        """Imprime un resumen del estudiante (ID, nombre, conteo y nota final)"""
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    """Función de arranque que ejecuta un ejemplo mínimo"""
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
