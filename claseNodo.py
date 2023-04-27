import random

# Clases que utilizaremos para crear el grafo

# Clase nodo contiene el nombre del nodo que es una letra
#                     el valor de la heuristica
#                     las veces que se expandio el nodo
#                     aristas que corresponde a la clase Arista  
class Nodo:
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
         
# creo que este metodo no tiene uso
    def recorrer(self):
        print(self.nombre + " " + self.heuristica)  
        for arista in self.aristas:
            print(" ->", arista.nombre," ",arista.heuristica)
            arista.nodo.recorrer()

# Clase arista contiene el nombre de la arista que son dos letras, la del nodo inicial y el final.
#                       el valor de la heuristica, mejor dicho el costo de la arista                      
#                       nodo que corresponde a la clase Nodo, este es el nodo al cual la arista va dirigida 
class Arista:
    def __init__(self,nombre,heuristica,nodo):
        self.nombre = nombre
        self.heuristica=heuristica
        self.nodo=nodo


# Clase ArbolDecision contiene el nodo de la clase Nodo, es decir, contiene al nodo el cual se expandio en la decision
#                     el nodo padre, ya que se desea obtener el camino de la rama que encontro la solucion
#                     las heuristica es el valor o costo de la decision dependiendo del tipo de busqueda que se use
#                     los hijos que corresponden a otra instancia del arbol de decision
#                     cada vez que se crea un variable de decicion se expande el nodo que se tomo en la hoja
class ArbolDecision:
    def __init__(self,nodo,nodo_padre,valor):
        self.nodo = nodo
        self.nodo_padre=nodo_padre
        self.heuristica=valor
        self.nodoshijos = []
        self.valoracumulado=0
        nodo.expandir()

    def agregar_nodohijo(self, nodo):   
        self.nodoshijos.append(nodo)
    
    def acumular(self,valor):
        self.valoracumulado += valor

# Si dos elementos tienen igual heuristica, se mezcla aleatoriamente su orden
    def __lt__(self, other):
        if self.heuristica == other.heuristica:
            return True
        else:
            return self.heuristica < other.heuristica