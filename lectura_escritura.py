lista = ['tercera linea \n', 'cuarta linea \n']

fichero = open("archivo2.txt", "w")
fichero.write("primera linea \n")
fichero.write("segunda linea \n")
fichero.writelines(lista)
fichero.close()

fichero = open("archivo2.txt", "r")
print(fichero.read())
fichero.seek(0)
# seek es para volver al puntero 0
print(fichero.readline())
fichero.seek(0)
print(fichero.readlines())
fichero.close()
