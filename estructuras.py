# Se crea una estructura de datos PriorityQueue

class PriorityQueue:

    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, nodo, prioridad):
        self.queue.append((prioridad, nodo))
        self.queue.sort()

    def delete(self, nodo):
        if self.is_empty():
            return None
        else:
            for i, (prioridad, n) in enumerate(self.queue):
                if n == nodo:
                    self.queue.pop(i)
                    return n
            return None

    def get_first_element(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0][1]

    def get_element(self, nodo):
        for prioridad, n in self.queue:
            if n == nodo:
                return (prioridad, n)
        return None
    
    def print_queue(self):
        if self.is_empty():
            print("La cola de prioridad está vacía")
        else:
            for prioridad, nodo in self.queue:
                print(f"Prioridad: {prioridad}, Nodo: {nodo.nodo.nombre}")