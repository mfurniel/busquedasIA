import claseNodo
import random
import estructuras

# Búsqueda en profundidad (escogiendo un sucesor al azar) o DFS "Depth-First Search"
def dfs_azar(initial,goal):
    arbol_decision = claseNodo.ArbolDecision(initial,None,0)
    punta = arbol_decision

    if initial == goal:
        return arbol_decision

    while punta.nodo != goal:
        aleatorio = random.randint(0, len(punta.nodo.aristas)-1)
        nodo_seleccionado = punta.nodo.aristas[aleatorio].nodo
        aux = claseNodo.ArbolDecision(nodo_seleccionado,punta,punta.heuristica + punta.nodo.aristas[aleatorio].heuristica)
        punta.agregar_nodohijo(aux)
        punta=aux
       
    return arbol_decision

# Búsqueda por costo uniforme o UCS "Uniform Cost Search"
def ucs(inicial,final):
   
    nodos_actuales = estructuras.PriorityQueue()
    arbol_decision = claseNodo.ArbolDecision(inicial,None,0)
    punta = arbol_decision
    nodos_actuales.insert(punta,punta.heuristica)
    explorados=[]
    explorados.append(inicial.nombre)
    
    while nodos_actuales.is_empty() != True:

        if nodos_actuales.checknode(final.nombre):
            punta=nodos_actuales.getnode(final.nombre)
            break

        punta = nodos_actuales.get_first_element()
        nodos_actuales.delete(punta)
        
        if punta.nodo == final:
             break
       
        for i in punta.nodo.aristas:

            if not nodos_actuales.checknode(i.nodo.nombre):
                if i.nodo.nombre not in explorados:        
                    aux = claseNodo.ArbolDecision(i.nodo,punta,(int(punta.heuristica) + int(i.heuristica)))
                    punta.agregar_nodohijo(aux)
                    explorados.append(aux.nodo.nombre)        
                    nodos_actuales.insert(aux,aux.heuristica)
                    explorados.append(punta.nodo.nombre)
                elif i.nodo.nombre in explorados:
                    if nodos_actuales.checknode(i.nodo.nombre) and (nodos_actuales.getnode(i.nodo.nombre).heuristica > (int(punta.heuristica) + int(i.heuristica))):   
                        aux = claseNodo.ArbolDecision(i.nodo,punta,(int(punta.heuristica) + int(i.heuristica)))
                        punta.agregar_nodohijo(aux)
                        nodos_actuales.delete(nodos_actuales.getnode(aux.nodo.nombre))
                        nodos_actuales.insert(aux,aux.heuristica)

    # la punta parte por el nodo final porque puede volver hacia la raiz
    # por ende tener en cuenta que no esta en orden de initial a goal
    return punta

# Busqueda Greedy
def greedy(initial,goal):

    arbol_decision = claseNodo.ArbolDecision(initial,None,0)
    punta = arbol_decision

    if initial == goal:
        return arbol_decision

    while punta.nodo != goal:
        nodo_seleccionado = punta.nodo.aristas[0].nodo
        costo = punta.nodo.aristas[0].heuristica
        for a in punta.nodo.aristas:
            if nodo_seleccionado.heuristica > a.nodo.heuristica:
                nodo_seleccionado = a.nodo
                costo = a.heuristica       
            if nodo_seleccionado.heuristica == a.nodo.heuristica:
                if random.random()==0:
                    nodo_seleccionado = a.nodo
                    costo = a.heuristica 
        aux = claseNodo.ArbolDecision(nodo_seleccionado,punta,punta.heuristica + costo)
        punta.agregar_nodohijo(aux)
        punta=aux
       
    return arbol_decision
    
def a_estrella(inicial,final):
    
    nodos_actuales = estructuras.PriorityQueue()
    arbol_desicion = claseNodo.ArbolDecision(inicial,None,0)
    punta = arbol_desicion
    nodos_actuales.insert(punta,punta.heuristica)
    explorados=[]
    explorados.append(inicial.nombre)

    while nodos_actuales.is_empty() != True:

        if nodos_actuales.checknode(final.nombre):
            punta=nodos_actuales.getnode(final.nombre)
            break

        punta = nodos_actuales.get_first_element()
        nodos_actuales.delete(punta)

        if punta.nodo == final:
             break
        
        for i in punta.nodo.aristas:
            if not nodos_actuales.checknode(i.nodo.nombre):
                if i.nodo.nombre not in explorados:     
                    valor_heuristico = punta.valoracumulado +int(i.nodo.heuristica) + int(i.heuristica)
                    aux = claseNodo.ArbolDecision(i.nodo,punta,punta.heuristica + int(i.heuristica))
                    aux.acumular(valor_heuristico)
                    punta.agregar_nodohijo(aux)
                    nodos_actuales.insert(aux,valor_heuristico)
            
    # la punta parte por el nodo final porque puede volver hacia la raiz
    # por ende tener en cuenta que no esta en orden de initial a goal
    return punta


     