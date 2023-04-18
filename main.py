import lectura
import imprimir
import claseNodo
import random

mapaDeGrafos = lectura.lecturagrafo('input.txt')
imprimir.imprimirmapa(mapaDeGrafos)
initial = lectura.nodoinicial('input.txt','inicial')
goal = lectura.nodoinicial('input.txt','final')

def bep_azar(inicial,final,mapa):

    raiz = claseNodo.Nodo(initial)
    punta = raiz
    aleatorio = random.randint(0, len(initial.aristas))
    raiz.agregar_hijo(raiz.aristas[aleatorio][0])
    punta = raiz.hijos[0]

    while punta != goal:
        aleatorio = random.randint(0, len(punta.aristas))
        punta.agregar_hijo(punta.aristas[aleatorio][0])
        punta = punta.hijos[0]
        
    return raiz

def bpcu_azar(inicial,final,mapa):

    return 0

def bg(inicial,final,mapa):

    return 0

def a_estrella(inicial,final,mapa):

    return 0