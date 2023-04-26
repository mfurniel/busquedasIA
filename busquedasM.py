import claseNodo
import random
import estructuras

def buscarNodo(nombre,mapa_de_nodos):
        for nodo in mapa_de_nodos:
             if nodo.nombre == nombre:
                  return nodo
    

def bep_azar(initial,goal):
    solucion = []
    punta=initial

    if initial == goal:
         return solucion
    else:
          solucion.append(punta)

    while punta != goal:
        aleatorio = random.randint(0, len(punta.aristas)-1)
        punta = punta.aristas[aleatorio].nodo
        solucion.append(punta)
    for a in solucion:
         print(a.nombre)
    return solucion



def bpcu(inicial,final):
    #print('-')
    nodos_actuales = estructuras.PriorityQueue()
    #print('-')
    arbol_desicion = claseNodo.ArbolDesicionM(inicial,None,0)
    #print('-')
    punta = arbol_desicion
    #print('-')
    #print(type(punta.heuristica))
    nodos_actuales.insert(punta,punta.heuristica)
    #print('-')
    
    #while punta.nodo != final:
    #print('-w')}
    flag = True
    while flag:
    
        for i in punta.nodo.aristas:
            print('-i-')
            print(i.nodo.nombre)
            print('-i-')
            #print('-wf')
            aux = claseNodo.ArbolDesicionM(i.nodo,punta,(int(punta.heuristica) + int(i.heuristica)))
            print('--wf')
            punta.agregar_nodohijo(aux)
            print(punta.nodo.nombre)
            print(aux.nodo.nombre)
            print('---wf')
           
            # print(aux.nodo.nombre)
            # print(aux.heuristica)
        
            nodos_actuales.insert(aux,aux.heuristica)
            #print('----wf')
            print(punta.nodo.nombre)
            nodos_actuales.print_queue()
            if aux.nodo==final:
                print('ifinal')
                print(punta.nodo.nombre)
                print(aux.nodo.nombre)
                punta = aux
                print('--ifinal--')
                print(punta.nodo.nombre)
                print(aux.nodo.nombre)
                flag=False
                print('ifinal')
                break
            
        if punta.nodo == final:
             break
        
        print('compa')
        nodos_actuales.delete(punta)
        #print('---w')
        punta = nodos_actuales.get_first_element()
        print(punta.nodo.nombre)
        print(punta.nodo)
        print(final)
        print('--compa')
        
    #print('----w')
    nodos_actuales.print_queue()
    #print('-----w')    
    print(nodos_actuales.get_first_element().nodo.nombre)

    print(punta.nodo.nombre, " ", punta.heuristica)
    
    while True: 
        print(punta.nodo.nombre)
        if punta.nodo_padre == None:
            break
        punta=punta.nodo_padre
        
        
        

    return 0

def bg(initial,goal):
    solucion = []
    punta=initial

    if initial == goal:
         return solucion
    else:
          solucion.append(punta)

    while punta != goal:
        nodo_menor = min(punta.aristas, key=lambda arista: arista.nodo.heuristica).nodo
        print(nodo_menor.nombre)
        punta = nodo_menor
        solucion.append(punta)
    print('-')   
    for a in solucion:
         print(a.nombre)
    print('-')   
    return solucion
    
def a_estrella(inicial,final):
    #print('-')
    nodos_actuales = estructuras.PriorityQueue()
    #print('-')
    arbol_desicion = claseNodo.ArbolDesicionM(inicial,None,inicial.heuristica)
    #print('-')
    punta = arbol_desicion
    #print('-')
    #print(type(punta.heuristica))
    nodos_actuales.insert(punta,punta.heuristica)
    #print('-')
    
    #while punta.nodo != final:
    #print('-w')}
    flag = True
    while flag:
    
        for i in punta.nodo.aristas:
            print('-i-')
            print(i.nodo.nombre)
            print('-i-')
            #print('-wf')
            aux = claseNodo.ArbolDesicionM(i.nodo,punta,(int(i.nodo.heuristica) + int(i.heuristica)))
            print('--wf')
            punta.agregar_nodohijo(aux)
            print(punta.nodo.nombre)
            print(aux.nodo.nombre)
            print('---wf')
           
            # print(aux.nodo.nombre)
            # print(aux.heuristica)
        
            nodos_actuales.insert(aux,aux.heuristica)
            #print('----wf')
            print(punta.nodo.nombre)
            nodos_actuales.print_queue()
            if aux.nodo==final:
                print('ifinal')
                print(punta.nodo.nombre)
                print(aux.nodo.nombre)
                punta = aux
                print('--ifinal--')
                print(punta.nodo.nombre)
                print(aux.nodo.nombre)
                flag=False
                print('ifinal')
                break
            
        if punta.nodo == final:
             break
        
        print('compa')
        nodos_actuales.delete(punta)
        #print('---w')
        punta = nodos_actuales.get_first_element()
        print(punta.nodo.nombre)
        print(punta.nodo)
        print(final)
        print('--compa')
        
    #print('----w')
    nodos_actuales.print_queue()
    #print('-----w')    
    print(nodos_actuales.get_first_element().nodo.nombre)

    print(punta.nodo.nombre, " ", punta.heuristica)
    
    while True: 
        print(punta.nodo.nombre,' ', punta.heuristica)
        if punta.nodo_padre == None:
            break
        punta=punta.nodo_padre
        
        
        

    return 0


     