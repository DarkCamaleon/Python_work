import csv
import os


def registrar_trabajador(nombre_archivo):
    cantidad = int(input('cuantos trabajadores deseas ingresar? : '))
    with open(nombre_archivo, 'a') as archivo_csv:
        escribir = csv.writer(archivo_csv, delimiter=',')
        for row in range(cantidad):
            os.system('clear')
            nombre = input("nombre : ")
            departamento = input("departamento : ")
            cuidad = input(" cuidad : ")
            escribir.writerow([nombre, departamento, cuidad])


def mostrar_trabajadores(nombre_archivo):
    os.system('clear')
    with open(nombre_archivo, 'r') as archivo_csv:
        leer = csv.reader(archivo_csv)
        for row in leer:
            print("nombre : ", row[0])
            print("departamento : ", row[1])
            print("cuidad : ", row[2])
            print('*'*60)


def principal():
    archivo = os.path.join("trabajadores.csv")
    registrar_trabajador(archivo)
    mostrar_trabajadores(archivo)


principal()
