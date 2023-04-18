import claseNodo

def nodoinicial(nombre_archivo,cual):
    archivo = open(nombre_archivo, "r")
    contenido = archivo.readlines()
    archivo.close()
    seccionInicialFinal = contenido[0:2]
    nodo_incial = seccionInicialFinal[0].split()[1]
    nodo_final = seccionInicialFinal[1].split()[1]
    if cual == 'inicial':
        return nodo_incial
    if cual == 'final':
        return nodo_final
   

def lecturagrafo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    contenido = archivo.readlines()
    archivo.close()

    seccionInicialFinal = contenido[0:2]
    print( seccionInicialFinal[0])
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

    nodo_incial = seccionInicialFinal[0].split()[1]
    nodo_final = seccionInicialFinal[1].split()[1]

    arrayNodos = []

    for node in seccionNodos:
        nodo = claseNodo.NodoMapa(node.split()[0], node.split()[1])
        for aristas in seccionAristas:
            if node.split()[0] == aristas.split()[0]:
                nodo.agregar_arista(aristas.split()[1], aristas.split()[2])
        arrayNodos.append(nodo)

    return arrayNodos
