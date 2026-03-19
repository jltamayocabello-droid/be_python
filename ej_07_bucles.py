# for
for i in range(10):
    print(i)

for i in range(1, 11):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")

# while
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1

# break
for numero in range(1, 110):
    if numero == 35:
        break
    print(numero)

# continue
for numero in range(1, 110):
    if numero == 35:
        continue
    print(numero)