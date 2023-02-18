from random import randrange


class RandomGraph:
    # n è il numero di nodi del grafo
    def __init__(self, n):
        if n <= 0:
            raise (ValueError("Vertex value must be at least 1"))  # controlliamo che il numero di vertici sia almeno 1
        self.numVert = n  # numero di vertici
        self.vertices = {}  # set dei vertici
        for i in range(0, n):
            self.vertices[i] = (str(i))  # riempie il set dei vertici
        maxEdges = int((n * (n - 1)) / 2)  # numero massimo di archi in un grafo di n elementi
        numEdges = randrange(0, maxEdges)  # genera il numero di archi presenti
        self.edges = {}  # set di tuple
        self.adjacencyList = {}  # dichiariamo la lista di adiacenza
        for i in range(0, self.numVert):
            self.adjacencyList[i] = []  # inizializza la lista di adiacenza
        for i in range(0, numEdges):
            while True:  # crea due indici diversi
                v1 = randrange(0, self.numVert)
                v2 = randrange(0, self.numVert)
                if v1 != v2:
                    break
            if self.alreadyPresent(v1, v2):
                self.edges[i] = (v1, v2)
                self.adjacencyList[v1].append(v2)  # riempie la lista di adiacenza
                self.adjacencyList[v2].append(v1)
        self.numEdges = len(self.edges)

    def alreadyPresent(self, v1, v2):
        if v2 in self.adjacencyList[v1]:
            return False
        return True
