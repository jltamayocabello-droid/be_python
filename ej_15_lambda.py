def cuadrado(numero):
    return numero * numero

print(cuadrado(5))

resultado = (lambda numero: numero * numero)(8)
print(resultado)