print("Hola cursor")

# Recorre los números del 0 al 9 e imprime cada uno en una línea
for i in range(10):
    print(i)

# Función para verificar si un número es primo

def es_primo(n):
    """
    Devuelve True si n es un número primo, False en caso contrario.
    Un número primo es un entero mayor que 1 que solo es divisible
    entre 1 y él mismo (por ejemplo: 2, 3, 5, 7, 11).
    """
    # Los primos son enteros mayores que 1
    if n <= 1:
        return False
    # 2 es el único primo par
    if n == 2:
        return True
    # Cualquier otro par (4, 6, 8...) no es primo
    if n % 2 == 0:
        return False
    # Solo hace falta probar divisores impares hasta la raíz cuadrada de n.
    # Si n = a * b y a <= b, entonces a <= sqrt(n); si hubiera un divisor
    # mayor que sqrt(n), el otro factor sería menor y ya lo habríamos encontrado.
    i = 3
    while i * i <= n:
        if n % i == 0:
            # n es divisible por i, así que no es primo
            return False
        i += 2  # saltamos pares (ya descartamos divisibilidad por 2)
    # No encontramos ningún divisor: n es primo
    return True
# Ejemplos de uso
if __name__ == "__main__":
    for numero in [0, 1, 2, 3, 4, 17, 25, 29]:
        print(f"{numero} -> {'primo' if es_primo(numero) else 'no primo'}")