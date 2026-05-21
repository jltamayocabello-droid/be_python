# 1. Pedir al usuario la ruta de un archivo de texto.

archivo = input("Ingrese la ruta del archivo: ")
try:
    with open(archivo, "r", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:
    print("El archivo no existe")
    exit()

# 2. Leer el contenido del archivo.

 

 

# 3. Separar en palabras.

# 4. Contar número total de palabras.

 

 

# 5. (Opcional) Mostrar las 10 palabras más frecuentes y su conteo.

 