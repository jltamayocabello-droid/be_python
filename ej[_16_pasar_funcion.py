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

# Retorno de funciones
def crear_saludo():
    def saludo():
        print("Hola desde dentro")
    return saludo

function_saludo = crear_saludo()
function_saludo()
