class EdadInvalidaError(Exception):
    def __init__(self, mensaje="Edad invalida: debe ser mayor o igual a 18"):
        super().__init__(mensaje)

        def validar_edad(edad):
            if edad < 18:
                raise EdadInvalidaError(f"Edad {edad} es menor a 18")
            return "Edad válida"
        try:
            resultado = validar_edad(15)
        except EdadInvalidaError as eie:
            print(f"Excepción personalizada capturada: {eie}")
        else: 
            print(resultado)
        finally:
            print("Validación completa")