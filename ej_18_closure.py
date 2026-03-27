def crear_saludo(mensaje: str):
    def saludar():
        print(mensaje)
        
    return saludar

saludo_uno = crear_saludo("Hola desde Python")
saludo_uno()