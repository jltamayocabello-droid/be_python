# 1. Pedir al usuario la ruta de un archivo de texto.

archivo = input("Ingrese la ruta del archivo: ")
try:
    with open(archivo, "r", encoding="utf-8") as f:  

# 2. Leer el contenido del archivo.

 texto = f.read()
except FileNotFoundError:
    print("El archivo no existe")
    exit()
 
# 3. Separar en palabras.

import re
palabras = re.findall(r'\b\w+\b', texto.lower())

# 4. Contar número total de palabras.

total_palabras = len(palabras)
print(f"El total de palabras es: {total_palabras}")
 
# 5. (Opcional) Mostrar las 10 palabras más frecuentes y su conteo.

 contador = Counter(palabras)
 mas_frecuentes = contador.most_common(10)
 print(f"Las 10 palabras más frecuentes son: {mas_frecuentes}")

 for palabra, conteo in mas_frecuentes:
     print(f"{palabra}: {conteo}")