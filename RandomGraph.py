from random import randrange


class Graph:
    # n è il numero di nodi del grafo
    def __int__(self, n):
        if n <= 0:
            raise (ValueError("Vertex value must be at least 1"))  # controlliamo che il numero di vertici sia almeno 1
        self.nV = n  # numero di vertici
        self.v = {}  # set dei vertici
        for i in range(0, n):
            self.v[i] = (str(i))  # riempie il set dei vertici
        maxEdges = (n * (n - 1)) / 2  # numero massimo di archi in un grafo di n elementi
        self.nE = randrange(0, maxEdges)  # genera il numero di archi presenti
