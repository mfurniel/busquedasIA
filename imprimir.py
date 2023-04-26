
# Metodos para imprimir las soluciones de las busquedas con el formato de salida pedido

def imprimirmapa(arrayMapa):
    for elemento in arrayMapa:
        print('Nodo: ' + elemento.nombre + ' ' + 'Valor: ' + elemento.heuristica)
        print('Aristas:', end=" ")
        print(elemento.aristas)

def imprimirDFS(raiz):
    punta = raiz
    while True:
        print(punta.nodo.nombre, end="")
        if len(punta.nodoshijos) == 0:
            print('')
            print('Costo: ',punta.heuristica)
            while True:
                print(raiz.nodo.nombre,' ',raiz.nodo.expandido)
                if len(raiz.nodoshijos) == 0:
                    break
                raiz=raiz.nodoshijos[0]
            break
        print(" -> ", end="")
        punta=punta.nodoshijos[0]


# Se busca del final hacia adelante debido a que los nodos tienen sus nodos padres
# lo que me hace buscar el camino hacia atras a la raiz.
def impimirUCS(punta):
    aux = punta
    orden = []

    while True: 

        orden.append(aux.nodo)

        if aux.nodo_padre == None:

            orden.reverse()

            for i in range(len(orden)):
                if i == len(orden) - 1:
                    print(orden[i].nombre)
                else:
                    print(orden[i].nombre, '->', end='')
            print('Costo: ',punta.heuristica)
            for elemento in orden:
                print(elemento.nombre,' ',elemento.expandido)
            break

        aux=aux.nodo_padre

def imprimirGreedy(raiz):
    punta = raiz
    while True:
        print(punta.nodo.nombre, end="")
        if len(punta.nodoshijos) == 0:
            print('')
            print('Costo: ',punta.heuristica)
            while True:
                print(raiz.nodo.nombre,' ',raiz.nodo.expandido)
                if len(raiz.nodoshijos) == 0:
                    break
                raiz=raiz.nodoshijos[0]
            break
        print(" -> ", end="")
        punta=punta.nodoshijos[0]

# Se busca del final hacia adelante debido a que los nodos tienen sus nodos padres
# lo que me hace buscar el camino hacia atras a la raiz.
def impimirAEstrella(punta):
    
    aux = punta
    orden = []

    while True: 

        orden.append(aux.nodo)

        if aux.nodo_padre == None:

            orden.reverse()

            for i in range(len(orden)):
                if i == len(orden) - 1:
                    print(orden[i].nombre)
                else:
                    print(orden[i].nombre, '->', end='')
            print('Costo: ',punta.heuristica)
            for elemento in orden:
                print(elemento.nombre,' ',elemento.expandido)
            break

        aux=aux.nodo_padre

    return 0