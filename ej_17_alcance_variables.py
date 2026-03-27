# Variable local
def saludar() -> None:
    mensaje = "Local"
    print(mensaje)

saludar()

# Variables globales
mensaje_global = "Global"
print(mensaje_global)

def mostrar() -> None:
    global mensaje_global
    mensaje_global = "Global Modificado"
    print(mensaje_global)

mostrar()