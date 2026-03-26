def saludar() -> None:
    print("Función de prueba")

def ejecutar(funcion) -> None:
    funcion()

ejecutar(saludar)

# Funciones con parametros
def saludo(nombre: str) -> None:
    print("Hola", nombre)

saludo("Pedro")

def ejecutando(funcion, valor) -> None:
    funcion(valor)

ejecutando(saludo, "Romana")