import claseNodo
import random
import estructuras

def buscarNodo(nombre,mapa_de_nodos):
        for nodo in mapa_de_nodos:
             if nodo.nombre == nombre:
                  return nodo
    

def bep_azar(initial,goal,mapa_de_nodos):

    raiz = claseNodo.Nodo(initial)
    # print('num')
    # print(len(initial.aristas))
    punta = raiz
    # print('-')
    # print(raiz.valor.nombre)
    # print(raiz.valor.aristas)
    # print('-')
    # print('--')
    num=len(initial.aristas)
    num=num-1
    aleatorio = random.randint(0, num)
    # print(aleatorio)
    # print('--')
    # print('---')
    # print('--x')
   
    
    hijo_buscado = buscarNodo(initial.aristas[aleatorio][0],mapa_de_nodos)
    hoja = claseNodo.Nodo(hijo_buscado)
    raiz.agregar_hijo(hoja)
    print(hijo_buscado.nombre)
    #print('---')
    punta = raiz.hijos[0]
    print('zzz')
    print(punta.valor.nombre)
    print('zzz')

    while punta.valor != goal:
        print('-')
        print(punta.valor.aristas)
        print('-0')
        auxnum=len(punta.valor.aristas)
        auxnum=auxnum-1
        print(auxnum)
        aleatorio = random.randint(0, auxnum)
        print('-')
        hijo_buscado = buscarNodo(punta.valor.aristas[aleatorio][0],mapa_de_nodos)
        hoja = claseNodo.Nodo(hijo_buscado)
        punta.agregar_hijo(hoja)
        punta = punta.hijos[0]
    print('--raiz--')  
    raiz.recorrer()
    print('--raiz--')    
    return raiz

def bpcu(inicial,final,mapa_de_nodos):
    print('-')
    cola_de_prioridad = estructuras.PriorityQueue()
    print('--')
    raiz = claseNodo.Nodo(inicial,0)
    punta = raiz
    print('---')
    num=len(inicial.aristas)
    num=num
    print('----')
    if inicial==final:
         return final
    print('-----')
    for i in range(num):
        print('-f')
        hijo_buscado = buscarNodo(inicial.aristas[i][0],mapa_de_nodos)
        hoja = claseNodo.Nodo(hijo_buscado,int(inicial.aristas[i][1]))
        cola_de_prioridad.insert(hoja,int(hoja.valor.aristas[i][1]))
        raiz.agregar_hijo(hoja)
    print('-----for')
    punta = cola_de_prioridad.queue[0][1]
    print(punta.valor.nombre)
    print('-for')
    while punta.valor != final:
        print('-1')
        num=len(punta.valor.aristas)
        num=num
        print('-2')
        cola_de_prioridad.delete(punta)
        print('-3')
        for i in range(num):
            print('-4for')
            hijo_buscado = buscarNodo(punta.valor.aristas[i][0],mapa_de_nodos)
            print('-5for')
            hoja = claseNodo.Nodo(hijo_buscado,int(punta.valor.aristas[i][1])+punta.costoacumulado)
            print('-6for')
            cola_de_prioridad.insert(hoja,int(hoja.costoacumulado))
            punta.agregar_hijo(hoja)
        punta = cola_de_prioridad.queue[0][1]

    return 0

def bg(inicial,final,mapa):

    return 0

def a_estrella(inicial,final,mapa):

    return 0     