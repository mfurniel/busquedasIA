class NodoMapa:
    def __init__(self,nombre,heuristica):
        self.nombre = nombre
        self.heuristica = heuristica
        self.aristas = []

    def agregar_arista(self, nodo_destino, valor_arista):
        self.aristas.append((nodo_destino, valor_arista))

class Nodo:
    def __init__(self, nodoMapa):
        self.valor = nodoMapa
        self.hijos = []
    
    def agregar_hijo(self, nodoMapa):
        self.hijos.append(nodoMapa)    

    def eliminar_hijo(self,nodoMapa):
         self.hijos.remove(nodoMapa)

    def recorrer(self):
        print(self.valor)
        for hijo in self.hijos:
            hijo.recorrer()