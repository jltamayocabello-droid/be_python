import csv

with open("datos.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        print(fila)