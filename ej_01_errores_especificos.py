entrada = input("Ingresa un número para dividir 10 por el :")

try:
    numero = float(entrada)
    resultado = 10 / numero
except ValueError as ve:
    print(f"Error de valor: {ve} por favor ingresa un número válido")
except ZeroDivisionError as zde:
    print(f"Error de división: {zde} no se pede dividir por cero")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print(f"Resultado de la división: {resultado}")
finally: 
    print("Operación finalizada")