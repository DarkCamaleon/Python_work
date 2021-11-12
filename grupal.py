import json
import pickle
import os

with open('Tarea/archivo.json') as fichero:
    contenido = json.load(fichero)

    # for elemento in contenido.values():
    #     print(elemento)
    #     print(elemento.get("nombre_producto"))

contenido['nombre_producto']['polera'] = 100


for elemento, valor in contenido['registro_ventas'].items():
    comision = valor * 0.1
    contenido['comisiones']["comision_" + elemento] = comision


archivo = json.dumps(contenido)

with open('Tarea/archivo.json', 'w') as fichero:
    fichero.writelines(archivo)


ruta_archivo = os.path.join("Tarea/archivo.json", contenido)

with open(ruta_archivo, "wb") as fichero:
    pickle.dump(contenido, fichero)


# with open(ruta_archivo, "rb") as fichero:
#     lista = pickle.load(fichero)
#     print(lista)

print(fichero)

