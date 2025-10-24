"""Este módulo gestiona estudiantes y sus notas."""
from word2number import w2n


class Student:

    """Clase para almacenar y procesar información del estudiante."""

    def __init__(self, student_id, name):
        # Validación suave (no crashea)
        if not isinstance(student_id, str) or not student_id.strip():
            print("Error: ID vacío o inválido. Se asigna 'UNKNOWN'.")
            student_id = "UNKNOWN"
        if not isinstance(name, str) or not name.strip():
            print("Error: Nombre vacío o inválido. Se asigna 'UNKNOWN'.")
            name = "UNKNOWN"

        self.id = student_id.strip()
        self.name = name.strip()
        self.gradez = []          # lista de floats válidos [0..100]
        self.is_passed = False    # bool
        self.honor = False        # bool
        self.letter = None        # 'A'..'F'

    def add_grades(self, g):
        """
        Agrega una nueva nota/calificación a la lista de notas del estudiante
        :param g: La nota a añadir.
        """
        value = None

        # Intentar convertir: ya-numérico → float directo
        if isinstance(g, (int, float)):
            value = float(g)
        elif isinstance(g, str):
            s = g.strip().lower()
            # ¿cadena de dígitos simple?
            if s.replace('.', '', 1).isdigit():
                try:
                    value = float(s)
                except ValueError:
                    value = None
            else:
                # Intento con word2number (e.g., "fifty five")
                try:
                    value = float(w2n.word_to_num(s))
                except (ValueError, TypeError):
                    value = None
        else:
            value = None

        # Validaciones finales
        if value is None:
            print(f"Error: la nota '{g}' no es numérica. Se ignora.")
            return False

        if not 0.0 <= value <= 100.0:
            print(f"Error: la nota {value} está fuera de rango (0–100).")
            return False

        self.gradez.append(value)
        return True

    def _letter_from_average(self, avg):
        if avg >= 90.0:
            return "A"
        elif avg >= 80.0:
            return "B"
        elif avg >= 70.0:
            return "C"
        elif avg >= 60.0:
            return "D"
        else:
            return "F"

    def calcaverage(self):
        """
        Calcula y devuelve el promedio de las notas (gradez) del estudiante.

        :returns: El promedio de las notas o 0 si no hay notas.
        :rtype: float
        """
        if not self.gradez:
            avg = 0.0
        else:
            avg = sum(self.gradez) / len(self.gradez)

        # Determinar letra
        self.letter = self._letter_from_average(avg)
        # Pass/Fail
        self.is_passed = avg >= 60.0
        return avg

    def check_honor(self):
        """
        Verifica si el promedio del estudiante supera los 90 puntos.
        """
        avg = self.calcaverage()
        self.honor = avg >= 90.0
        return self.honor

    def delete_grade(self, index):
        """
        Elimina la nota del estudiante.
        """
        if not isinstance(index, int):
            print("Error: el índice debe ser entero.")
            return False

        if 0 <= index < len(self.gradez):
            removed = self.gradez.pop(index)
            print(f"Nota eliminada (índice {index}): {removed}")
            return True
        else:
            print(
                f"Error: índice fuera de rango. "
                f"Notas totales: {len(self.gradez)}"
            )
            return False

    def delete_grade_by_value(self, value):
        """
        Elimina por valor exacto (float). Si no existe, informa y no crashea.
        """
        try:
            value = float(value)
        except (TypeError, ValueError):
            print(f"Error: valor '{value}' inválido para eliminar.")
            return False

        for i, v in enumerate(self.gradez):
            if v == value:
                self.gradez.pop(i)
                print(f"Nota eliminada (valor {value}) en índice {i}.")
                return True

        print(f"No se encontró la nota con valor {value}.")
        return False

    def report(self):  # broken format
        """
        Imprime un resumen del estudiante (ID, nombre, conteo y nota final)
        """
        avg = self.calcaverage()
        passed_text = "Passed" if self.is_passed else "Failed"
        honor_text = "Yes" if self.honor else "No"

        lines = [
            f"Student ID      : {self.id}",
            f"Student Name    : {self.name}",
            f"Number of Grades: {len(self.gradez)}",
            f"Average Grade   : {avg:.2f}",
            f"Letter Grade    : {self.letter}",
            f"Pass/Fail       : {passed_text}",
            f"Honor Roll      : {honor_text}",
        ]
        summary = "\n".join(lines)
        print(summary)
        return summary


def startrun():
    """Función de arranque que ejecuta un ejemplo mínimo"""
    # ---- Estudiante 1: todo correcto ----
    s1 = Student("S-001", "Alice")
    s1.add_grades(100)          # válido
    s1.add_grades("82.5")       # string numérica válida
    s1.add_grades("Ninety five")      # palabra -> 50
    s1.calcaverage()
    s1.check_honor()
    print("== Reporte Estudiante 1 (OK) ==")
    s1.report()

    print("\n" + "-" * 40 + "\n")

    # ---- Estudiante 2: control de errores ----
    # ID y nombre vacíos -> se asigna 'UNKNOWN' con mensajes
    s2 = Student("", "   ")

    # Notas inválidas (no crashean, se ignoran con mensajes)
    s2.add_grades(-5)           # fuera de rango
    s2.add_grades("hello")      # no numérico
    s2.add_grades(110)          # fuera de rango
    s2.add_grades("101.0")      # fuera de rango
    s2.add_grades(None)         # tipo inválido
    s2.add_grades("Fifty")     # válida -> 90.0
    s2.add_grades(55.0)         # válida
    s2.add_grades("  45  ")     # válida -> 45.0

    # Eliminaciones con error y éxito
    s2.delete_grade(999)        # índice fuera de rango
    s2.delete_grade("two")      # índice no entero
    s2.delete_grade_by_value("abc")   # valor inválido
    s2.delete_grade_by_value(77.7)    # no existe
    s2.delete_grade_by_value(45.0)    # existe -> se elimina

    s2.calcaverage()
    s2.check_honor()
    print("== Reporte Estudiante 2 (con errores) ==")
    s2.report()


startrun()
