import re
from collections import Counter


def contar_palabras(texto: str) -> int:
    """Cuenta las palabras en un texto (letras/números separados por no-palabra)."""
    palabras = re.findall(r"\b\w+\b", texto.lower())
    return len(palabras)


if __name__ == "__main__":
    # 1. y 2. Pedir al usuario la ruta de un archivo de texto y leer el contenido.

    archivo = input("Ingrese la ruta del archivo: ")
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            texto = f.read()
    except FileNotFoundError:
        print("El archivo no existe")
        exit()

    # 3. y 4. Separar y contar palabras.

    palabras = re.findall(r"\b\w+\b", texto.lower())
    total_palabras = contar_palabras(texto)
    print(f"El total de palabras es: {total_palabras}")

    # 5. (Opcional) Mostrar las 10 palabras más frecuentes y su conteo.

    contador = Counter(palabras)
    mas_frecuentes = contador.most_common(10)
    print(f"Las 10 palabras más frecuentes son: {mas_frecuentes}")

    for palabra, conteo in mas_frecuentes:
        print(f"{palabra}: {conteo}")