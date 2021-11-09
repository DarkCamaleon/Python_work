import os

ruta_archivo = os.path.join("binario.bin")

with open("binario.bin", "wb") as archivo:
    archivo.write(b"hola soy un archivo creado desde python")

with open(ruta_archivo, "rb") as binario:
    print(binario.read())
