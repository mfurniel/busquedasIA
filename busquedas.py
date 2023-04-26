import claseNodo
import random
import estructuras

# Búsqueda en profundidad (escogiendo un sucesor al azar) o DFS "Depth-First Search"
def dfs_azar(initial,goal):
    arbol_decision = claseNodo.ArbolDesicionM(initial,None,0)
    punta = arbol_decision

    if initial == goal:
        return arbol_decision

    while punta.nodo != goal:
        aleatorio = random.randint(0, len(punta.nodo.aristas)-1)
        nodo_seleccionado = punta.nodo.aristas[aleatorio].nodo
        aux = claseNodo.ArbolDesicionM(nodo_seleccionado,punta,punta.heuristica + punta.nodo.aristas[aleatorio].heuristica)
        punta.agregar_nodohijo(aux)
        punta=aux

    nodo_actual=arbol_decision

    # while True:
    #     print(nodo_actual.nodo.nombre," ",nodo_actual.heuristica)
    #     if  len(nodo_actual.nodoshijos)==0:
    #         break
    #     nodo_actual = nodo_actual.nodoshijos[0]
       
    return arbol_decision

# Búsqueda por costo uniforme o UCS "Uniform Cost Search"
def ucs(inicial,final):
   
    nodos_actuales = estructuras.PriorityQueue()
    arbol_decision = claseNodo.ArbolDesicionM(inicial,None,0)
    punta = arbol_decision
    nodos_actuales.insert(punta,punta.heuristica)
   
    flag = True
    while flag:
        for i in punta.nodo.aristas:         
            aux = claseNodo.ArbolDesicionM(i.nodo,punta,(int(punta.heuristica) + int(i.heuristica)))
            punta.agregar_nodohijo(aux)        
            nodos_actuales.insert(aux,aux.heuristica)
            if aux.nodo==final:
                punta = aux
                flag=False
                break
        if punta.nodo == final:
             break
        nodos_actuales.delete(punta)
        punta = nodos_actuales.get_first_element()

    # la punta parte por el nodo final porque puede volver hacia la raiz
    # por ende tener en cuenta que no esta en orden de initial a goal
    return punta

def greedy(initial,goal):

    arbol_decision = claseNodo.ArbolDesicionM(initial,None,initial.heuristica)
    punta = arbol_decision

    if initial == goal:
        return arbol_decision

    while punta.nodo != goal:
        # aleatorio = random.randint(0, len(punta.nodo.aristas)-1)
        # nodo_seleccionado = punta.nodo.aristas[aleatorio].nodo
        nodo_seleccionado = punta.nodo.aristas[0].nodo

        for a in punta.nodo.aristas:
            if nodo_seleccionado.heuristica > a.nodo.heuristica:
                nodo_seleccionado = a.nodo       
            if nodo_seleccionado.heuristica == a.nodo.heuristica:
                if random.random()==0:
                    nodo_seleccionado = a.nodo
  
        aux = claseNodo.ArbolDesicionM(nodo_seleccionado,punta,punta.heuristica + nodo_seleccionado.heuristica)
        punta.agregar_nodohijo(aux)
        punta=aux

    # nodo_actual=arbol_decision

    # while True:
    #     print(nodo_actual.nodo.nombre," ",nodo_actual.heuristica)
    #     if  len(nodo_actual.nodoshijos)==0:
    #         break
    #     nodo_actual = nodo_actual.nodoshijos[0]
       
    return arbol_decision

    # solucion = []
    # punta=initial

    # if initial == goal:
    #      return solucion
    # else:
    #       solucion.append(punta)

    # while punta != goal:
    #     nodo_menor = min(punta.aristas, key=lambda arista: arista.nodo.heuristica).nodo
    #     punta = nodo_menor
    #     solucion.append(punta)   
   
    # return solucion
    
def a_estrella(inicial,final):
    
    nodos_actuales = estructuras.PriorityQueue()
    arbol_desicion = claseNodo.ArbolDesicionM(inicial,None,inicial.heuristica)
    punta = arbol_desicion
    nodos_actuales.insert(punta,punta.heuristica)

    flag = True
    while flag:
    
        for i in punta.nodo.aristas:
            aux = claseNodo.ArbolDesicionM(i.nodo,punta,(int(i.nodo.heuristica) + int(i.heuristica)))
            punta.agregar_nodohijo(aux)
            nodos_actuales.insert(aux,aux.heuristica)
            #nodos_actuales.print_queue()

            if aux.nodo==final:
                punta = aux
                flag=False
                break
            
        if punta.nodo == final:
             break
        
        nodos_actuales.delete(punta)
        punta = nodos_actuales.get_first_element()
    
    # while True: 
    #     print(punta.nodo.nombre,' ', punta.heuristica)
    #     if punta.nodo_padre == None:
    #         break
    #     punta=punta.nodo_padre

    return punta


     