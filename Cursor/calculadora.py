def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

# Clave: símbolo de la operación → función que recibe (a, b)
operaciones = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir,
}

while True:
    op = input("Operación (+, -, *, /) o 'salir': ").strip()

    if op.lower() == "salir":
        print("Hasta luego.")
        break

    if op not in operaciones:
        print("Operación no válida. Usa +, -, * o /")
        continue

    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        resultado = operaciones[op](a, b)
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")