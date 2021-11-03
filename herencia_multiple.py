class PersonalUniversitario:
    tipo = "humano"


class Profesor(PersonalUniversitario):
    materia = "programacion"

    def dictar_clases(self):
        print("dictando clases...")


class Alumno(PersonalUniversitario):
    carrera = "informatica"
    semestres = 6
    materia = "modelamiento de bases de datos"

    def dar_examen(self):
        print("rindiendo examen..")


class ProfesorAyudante(Profesor, Alumno):
    pass


ayudante1 = ProfesorAyudante()

ayudante1.semestres
ayudante1.dar_examen()

print(ProfesorAyudante.__mro__)
