import pickle

datos = {
    "usuario": "admin",
    "nivel": 10
}

with open("datos.pkl", "wb") as archivo:
    pickle.dump(datos, archivo)

with open("datos.pkl", "rb") as archivo:
    datos_cargados = pickle.load(archivo)
print(datos_cargados)    