def mi_decorador(funcion):
    def envoltura():
        print("antes de ejecutar la función")
        funcion()
        print("Despues de ejecutar la función")
    return envoltura

def saludar():
    print("Soy Saludar")

hola = mi_decorador(saludar)
hola()

@mi_decorador
def otro_saludar():
    print("Soy Otro Saludar")
