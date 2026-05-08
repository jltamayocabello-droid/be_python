class Grupo:
    def __init__(self, miembros):
        self.miembros = miembros

    def __len__(self):
        return len(self.miembros)
    
grupo = Grupo(["Ana", "Luis", "Carlos"])
print(len(grupo))