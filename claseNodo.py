class Nodo:
    def __init__(self,nombre,heuristica):
        self.nombre = nombre
        self.heuristica = heuristica
        self.aristas = []

    def agregar_arista(self, nodo_destino, valor_arista):
        self.aristas.append((nodo_destino, valor_arista))


