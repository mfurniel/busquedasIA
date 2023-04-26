# BusquedasIA
Ejercicio 5 Tarea Individual IA

5.- Programación. Debe adjuntar un enlace a repositorio github con su código fuente documentado e instrucciones para su ejecución (se descontará puntaje de no contar con una documentación adecuada y/o instrucciones). Su código debe ser creado en C, C++ o Python, debe ser original (se comparará con el de sus compañeros y de otros repositorios), y no se pueden utilizar bibliotecas más allá de las que facilitan el uso de listas o arrays (por ej., numpy en Python). Cualquier evidencia de copia implicará una nota 1.0 en la evaluación.
 
5.1.- (25 pts) Implemente un programa (en C, C++ o Python) que, utilizando una estructura de búsqueda tipo árbol, encuentre una solución para el problema de encontrar una ruta entre A y H, diagramado en la Figura 1. Debe utilizar los siguientes métodos: 
- Búsqueda en profundidad (escogiendo un sucesor al azar) 
- Búsqueda por costo uniforme
- Búsqueda greedy 
- A*

Para cada tipo de búsqueda, su código debe retornar:
- El camino encontrado y su costo (y si es la solución óptima, que ud. puede calcular a mano) 
- Cantidad de nodos expandidos (veces por nodo y en total) 

Su código debe leer el problema (grafo) desde un archivo .txt con el siguiente formato:   
Init: `<nodo_inicial>`  
Goal: `<nodo_objetivo>`  
`<Nodo1>` `<valor_heuristica1>`  
`<Nodo2>` `<valor_heurística2>`  
…..
`<Nodo1>`, `<nodo2>`, `<costo>` // en el caso en que exista una arista entre nodo1 y nodo2
…..

Su código podría ser evaluado, además, cambiando los nodos de inicio y/o objetivo. 
El formato de salida debe ser: 
Nodo_inicial → nodo1 → nodo2 …->nodo_objetivo 
Costo: <costo>
`<nodo_inicial>`: número de veces que se expandió
`<nodo1>`: número de veces que se expandió
…. 

5.2 .- (10 pts) Responda: - ¿Qué puede decir de la comparación entre los métodos implementados? En concreto, los que encontraron la solución óptima, a qué se debió? Y los que no, ¿por qué no la encontraron? - De los métodos vistos en clase, ¿hay alguno que NO retorne una solución (es decir, que se mantenga realizando búsqueda ad infinitum) en este problema? Si es así, cuál? Y si no, por qué no?

<img src="/imagen_grafo.png" alt="texto alternativo">
