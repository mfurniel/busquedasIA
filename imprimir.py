
def imprimirmapa(arrayMapa):
    for elemento in arrayMapa:
        print('Nodo: ' + elemento.nombre + ' ' + 'Valor: ' + elemento.heuristica)
        print('Aristas:', end=" ")
        print(elemento.aristas)