import pickle
import os

ruta_archivo = os.path.join("lista_cursos")
lista_cursos = ['python', 'java', 'javascripts', 'uxui']

with open(ruta_archivo, "wb") as fichero:
    pickle.dump(lista_cursos, fichero)
    # encrisptar el archivo


with open(ruta_archivo, "rb") as fichero:
    lista = pickle.load(fichero)
    print(lista)
