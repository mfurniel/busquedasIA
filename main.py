import lectura
import imprimir
import claseNodo
import random
import busquedas
import busquedasM

variables_lectura = lectura.lecturagrafoM('input.txt')

initial = variables_lectura[0]
goal = variables_lectura[1]
raiz_grafo = variables_lectura[2]

#busquedasM.bep_azar(initial,goal)

#busquedasM.bpcu(initial,goal)

#busquedasM.bg(initial,goal)

busquedasM.a_estrella(initial,goal)

#imprimir.imprimirmapa(mapa_de_nodos)

#print(initial.nombre)

#raiz_grafo.recorrer()

# initial = lectura.nodoinicial('input.txt','inicial')
# goal = lectura.nodoinicial('input.txt','final')
#busquedas.bep_azar(initial,goal,mapa_de_nodos)
#busquedas.bpcu(initial,goal,mapa_de_nodos)
print('salio?')



