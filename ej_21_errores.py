try:
    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
except FileNotFoundError as e: 
    print(f"Excepción capturada: {e}")
else:
    print("Archivo leído exitosamente:", contenido)
    archivo.close()
finally:
    print("Operación de archivo finalizada")