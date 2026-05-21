from collections.abc import Callable

Operacion = Callable[[float, float], float]


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


operaciones: dict[str, Operacion] = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir,
}


def main() -> None:
    while True:
        op: str = input("Operación (+, -, *, /) o 'salir': ").strip()

        if op.lower() == "salir":
            print("Hasta luego.")
            break

        if op not in operaciones:
            print("Operación no válida. Usa +, -, * o /")
            continue

        try:
            a: float = float(input("Primer número: "))
            b: float = float(input("Segundo número: "))
            resultado: float = operaciones[op](a, b)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
