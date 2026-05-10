with open("imagen1.png", "rb") as archivo_origen:
    contenido = archivo_origen.read()

with open("foto_copia.png", "wb") as archivo_destino:
    archivo_destino.write(contenido)

print("Imagen copiada exitosamente")