# OPERADORES ARTIMÉTICOS
a = 30
b = 3

# Suma
print(a + b)
# Resta
print(a - b)
# Multiplicación
print(a * b)
# División
print(a / b)
# Resto
print(a % b)
# División entera
print(a // b)
# Potencia
print(a ** b)

# OPERADORES RELACIONALES
edad = 24

# Mayor
print(edad > 18)
# Menor
print(edad < 18)
# Mayor o igual
print(edad >= 21)
# Menor o igual
print(edad <= 21)
# Igual
print(edad == 24)
# Diferente
print(edad != 33)

# OPERADORES LÓGICOS
es_mayor = True
tiene_permiso = False

print(es_mayor and tiene_permiso)
print(es_mayor or tiene_permiso)
print(not es_mayor)

edad = int(input("Ingrese su edad: "))
tiene_permiso = input("Tiene permiso? (s/n): ")
tiene_permiso = tiene_permiso == "s"
puede_ingresar = edad >= 18 and tiene_permiso
print(f"Puede ingresar: {puede_ingresar}")