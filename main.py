import lectura
import imprimir
import claseNodo
import random
import busquedas
import argparse
import sys

def dfs():
    solucion = busquedas.dfs_azar(initial,goal)
    imprimir.imprimirDFS(solucion)

def ucs():
    solucion =busquedas.ucs(initial,goal)
    imprimir.impimirUCS(solucion)

def greedy():
    solucion = busquedas.greedy(initial,goal)
    imprimir.imprimirGreedy(solucion)

def a_estrella():
    solucion =busquedas.a_estrella(initial,goal)
    imprimir.impimirAEstrella(solucion)

parser = argparse.ArgumentParser()
parser.add_argument("busqueda", help="nombre del busqueda a usar")
parser.add_argument("grafo", nargs='?', default="input.txt", help="nombre del archivo con el grafo")

args = parser.parse_args()

# aquí puedes usar los argumentos pasados desde la línea de comandos
print(args.busqueda)
print(args.grafo)

try:
    variables_lectura = lectura.lecturagrafo(args.grafo)
except FileNotFoundError:
    print("Error: el archivo no existe.")
    sys.exit()

variables_lectura = lectura.lecturagrafo(args.grafo)

initial = variables_lectura[0]
goal = variables_lectura[1]
raiz_grafo = variables_lectura[2]

switch = {
    'dfs': dfs,
    'ucs': ucs,
    'greedy': greedy,
    'a_estrella': a_estrella
}

if args.busqueda in switch:
    switch[args.busqueda]()  # ejecuta la función correspondiente al busqueda seleccionado
else:
    print('busqueda no válido')