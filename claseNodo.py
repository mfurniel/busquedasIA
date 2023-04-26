import random
class NodoMapa:
    def __init__(self,nombre,heuristica):
        self.nombre = nombre
        self.heuristica = heuristica
        self.aristas = []

    def agregar_arista(self, nodo_destino, valor_arista):
        self.aristas.append((nodo_destino, valor_arista))

class Nodo:
    def __init__(self, nodoMapa,cosoto_acumulado=0):
        self.valor = nodoMapa
        self.costoacumulado=cosoto_acumulado
        self.hijos = []
    
    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)    

    def eliminar_hijo(self,nodo):
         self.hijos.remove(nodo)

    def recorrer(self):
        print(self.valor.nombre)  
        for hijo in self.hijos:
            hijo.recorrer()

class NodoM:
    def __init__(self,nombre,heuristica):
        self.nombre = nombre
        self.heuristica=heuristica
        self.aristas = []
    
    def agregar_arista(self, arista):
        self.aristas.append(arista)    

    def eliminar_arista(self,arista):
         self.aristas.remove(arista)

    def recorrer(self):
        print(self.nombre + " " + self.heuristica)  
        for arista in self.aristas:
            print(" ->", arista.nombre," ",arista.heuristica)
            arista.nodo.recorrer()

class AristaM:
    def __init__(self,nombre,heuristica,nodo):
        self.nombre = nombre
        self.heuristica=heuristica
        self.nodo=nodo

class ArbolDesicionM:
    def __init__(self,nodo,nodo_padre,valor):
        self.nodo = nodo
        self.nodo_padre=nodo_padre
        self.heuristica=valor
        self.nodoshijos = []

    def agregar_nodohijo(self, nodo):   
        self.nodoshijos.append(nodo)
   
    #esta cosa no la entendi bien
    def __lt__(self, other):
        if self.heuristica == other.heuristica:
            # Si dos elementos tienen igual heuristica, se mezcla aleatoriamente su orden
            return random.choice([True, False])
        else:
            return self.heuristica < other.heuristica