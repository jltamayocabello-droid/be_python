while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")
    if entrada.lower() == "salir":
        print("Hasta luego.")
        break
    # Aquí va la lógica de tu calculadora u otra acción
    print(f"Recibiste: {entrada}")