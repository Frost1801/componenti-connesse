import csv
from typing import Optional

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from DisjointSetList import DisjointSetList, DisjointSetListHeuristic
from DisjointSetTree import DisjointSetTree, DisjointSetTreePathCompr
from RandomGraph import RandomGraph
from timeit import default_timer as timer


class Tester:
    def __init__(self, n: Optional[int]):  # n rappresenta la massima grandezza del grafo
        self.disjointSetN = None
        self.graphs = []
        self.start = 2  # iniziamo da due nodi
        self.stop = n + 1
        for i in range(self.start, self.stop):
            self.graphs.append(RandomGraph(i))  # crea il vettore dei grafi generati randomicamente alla creazione del
            # tester in modo da non perdere tempo per la creazione durante il test
        if len(self.graphs) != self.stop - self.start:
            raise (Exception("Graphs vector creation failed"))
        print("Graph creation successful!")
        self.resultArray = []
        self.labels = ["List", "List Heuristic", "Tree", "Tree p.c"]

    def runTests(self):
        # per ogni istanza di Disjoint set list gli applica il grafo, verifica il comportamento
        results = {}
        sets = self.createDisjointSets()
        for i in range(0, len(self.graphs)):
            results[i] = []  # dizionario di tuple dove elemento 1 è array di risultati e l' elemento 2 è intero

        for i in range(0, len(self.graphs)):
            for j in range(0, len(sets)):
                start = timer()
                result = sets[j].connectedComponents(self.graphs[i])
                end = timer()
                results[i].append((result, end - start))
        self.saveResults(results)
        self.fillResultArray(results)
        self.plotData(0,2)
        self.plotData(2,4)

    def saveResults(self, results):
        with open('times.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Nodes.n', 'DisjointType', 'Union time'])
            for i in range(0, len(results)):
                for j in range(0, len(results[i])):
                    filewriter.writerow([i + 2, j, results[i][j][1]])
            print("SUCCESSFULLY SAVED!")

    def fillResultArray(self, results):
        for i in range(0, self.disjointSetN):
            self.resultArray.append([])
        for j in range(0, self.disjointSetN):
            for i in range(0, len(results)):
                self.resultArray[j].append(results[i][j][1])

    def plotData(self, start, stop):
        n = self.fillXAxis()
        for i in range(start, stop):
            plt.plot(n, self.resultArray[i])
        labels = [self.labels[lb] for lb in range(start, stop)]
        plt.legend(labels, title="Tipologia Disjoint Set")
        plt.xlabel('Number graph nodes')
        plt.ylabel('Connected components time')
        plt.show()

    def fillXAxis(self):
        n = []
        for i in range(self.start, self.stop):
            n.append(i)
        return n

    def createDisjointSets(self):
        sets = [DisjointSetList(), DisjointSetListHeuristic(), DisjointSetTree(), DisjointSetTreePathCompr()]
        self.disjointSetN = 4
        return sets
