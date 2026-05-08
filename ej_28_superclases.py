class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def mostrar_info(self):
        return f"El empleado {self.nombre} tiene un salario de {self.salario}"
    
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} y trabaja en el departamento de {self.departamento}"
    
empleado = Empleado("Ana", 2000)
gerente = Gerente("Luis", 3000, "Finanzas")

print(empleado.mostrar_info())
print(gerente.mostrar_info())