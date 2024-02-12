import os
os.system('cls' if os.name == 'nt' else 'clear')

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError("Desencolar de una cola vacia")

    def esta_vacia(self):
        return len(self.elementos) == 0

cola = Cola()
cola.encolar('elemento1')
cola.encolar('elemento2')
cola.encolar('elemento3')

print("Elemento desencolado:", cola.desencolar())
print("Elemento desencolado:", cola.desencolar())
