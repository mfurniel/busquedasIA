import lectura
import imprimir
import busquedas
import argparse
import sys

#Definimos las funciones para llamar a las busquedas e imprimirla por pantalla

# Búsqueda en profundidad (escogiendo un sucesor al azar) o DFS "Depth-First Search"
def dfs():
    solucion = busquedas.dfs_azar(initial,goal)
    imprimir.imprimirDFS(solucion)

# Búsqueda por costo uniforme o UCS "Uniform Cost Search"
def ucs():
    solucion =busquedas.ucs(initial,goal)
    imprimir.impimirUCS(solucion)

# Busqueda Greedy
def greedy():
    solucion = busquedas.greedy(initial,goal)
    imprimir.imprimirGreedy(solucion)

# Busqueda A*
def a_estrella():
    solucion =busquedas.a_estrella(initial,goal)
    imprimir.impimirAEstrella(solucion)

# Se obtienen los argumentos al ejecutrar el programa
parser = argparse.ArgumentParser()
parser.add_argument("busqueda", help="nombre del busqueda a usar")
#dejamos el argumento por default de grafo com input.txt
parser.add_argument("grafo", nargs='?', default="input.txt", help="nombre del archivo con el grafo")

args = parser.parse_args()

# intentamos leer el archivo con el nombre seleccionado
#   si no existe el archivo arroja un error
try:
    variables_lectura = lectura.lecturagrafo(args.grafo)
except FileNotFoundError:
    print("Error: el archivo no existe.")
    sys.exit()

#procesamos el archivo txt con el formato de ingreso de los grafos
variables_lectura = lectura.lecturagrafo(args.grafo)

# nos arroja le nodo incial, nodo final y la raiz del grafo 
# se cae en cuenta que la variable arrayNodos no se ocupa,
# lo dejamos por si acaso ya que contiene todos los nodos y puede haber un caso donde un nodo
# este asilado (cosa que en el ejemplo no es asi)
initial = variables_lectura[0]
goal = variables_lectura[1]
arrayNodos = variables_lectura[2]

# hacemos una especie de "switch" para seleccionar la busqueda que queremos
switch = {
    'dfs': dfs,
    'ucs': ucs,
    'greedy': greedy,
    'a_estrella': a_estrella
}

# ejecuta la función correspondiente al busqueda seleccionado
if args.busqueda in switch:
    switch[args.busqueda]()  
else:
    print('busqueda no válido')