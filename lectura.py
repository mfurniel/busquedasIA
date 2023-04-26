import claseNodo

def lecturagrafo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    contenido = archivo.readlines()
    archivo.close()

    seccionInicialFinal = contenido[0:2]
    seccionNodos = []
    seccionAristas = []

    for elemento in contenido[2:]:
        partes = elemento.split(" ")
        if len(partes) == 2:
            seccionNodos.append(elemento)
        elif "," in partes[1]:
            seccionAristas.append(elemento)
        else:
            seccionNodos.append(elemento)

    for i in range(len(seccionAristas)):
        seccionAristas[i] = seccionAristas[i].replace(",", "")

    nodo_incial_name = seccionInicialFinal[0].split()[1]
    nodo_final_name = seccionInicialFinal[1].split()[1]

    nodo_inicial = None
    nodo_final = None

    arrayNodos = []

    for node in seccionNodos:
        nodo = claseNodo.NodoM(node.split()[0], int(node.split()[1]))
        if node.split()[0]==nodo_incial_name:
            nodo_inicial=nodo
        if node.split()[0]==nodo_final_name:
            nodo_final=nodo
        arrayNodos.append(nodo)

    for arista in seccionAristas:
        nodo_origen = None
        nodo_destino = None
        for nodo in arrayNodos:
            if nodo.nombre == arista.split()[0]:
                nodo_origen = nodo
            if nodo.nombre == arista.split()[1]:
                nodo_destino = nodo
            if nodo_origen and nodo_destino:
                break
        arista_nueva = claseNodo.AristaM(arista.split()[0]+arista.split()[1], int(arista.split()[2]), nodo_destino)
        nodo_origen.agregar_arista(arista_nueva)

    return nodo_inicial, nodo_final, arrayNodos[0]