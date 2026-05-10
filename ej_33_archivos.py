archivo = open("mensaje.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)

# Escribir en un archivo

archivo1 = open("salida.txt", "w")

archivo1.write("Resultado de la prueba\n")

archivo1.write("Caso número 1")
archivo1.close()

# Escribir utilizando with

with open("mensaje.txt", "r") as archivo:
    contenido = archivo.read()
print(contenido)
