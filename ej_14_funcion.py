def saludar() -> None:
    print("Función de prueba")

saludar() 

def sumar(num1: int, num2: int) -> int:
    return num1 + num2

resultado = sumar(100, 200)
print(resultado)

# Retorno de valores
def calcular_area(largo: float, ancho: float) -> float:
    area = largo * ancho
    return area

resultado_area = calcular_area(10, 5)
print(f"El area es: {resultado_area}")

# Parametro opcionales
def saludar_persona(nombre: str, mensaje: str="bienvenida" ) -> None:
    print(f"{nombre} {mensaje}")

saludar_persona("Elizabeth" "como estuvo tu viaje, bienvenida")