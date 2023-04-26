import random

class NodoM:
    def __init__(self,nombre,heuristica):
        self.nombre = nombre
        self.heuristica=heuristica
        self.expandido = 0
        self.aristas = []
    
    def expandir(self):
        self.expandido += 1
    
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
        nodo.expandir()

    def agregar_nodohijo(self, nodo):   
        self.nodoshijos.append(nodo)
   
    def __lt__(self, other):
        if self.heuristica == other.heuristica:
            # Si dos elementos tienen igual heuristica, se mezcla aleatoriamente su orden
            return random.choice([True, False])
        else:
            return self.heuristica < other.heuristica