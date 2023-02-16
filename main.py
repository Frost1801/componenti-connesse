# TODO IMPLEMENTAZIONE GRAFO
# creiamo prima i grafi per gli n valori e li memorizziamo in modo da non sprecare tempo per la creazione
# TODO CLASSE BASE UNION FIND

# TODO LISTA BASE
# TODO LISTA CON EURISTICA
# TODO ALBERI
# TODO SALVATAGGIO SU FILE CSV
import random

import numpy as np

import DisjoinedSetTree
from RandomGraph import RandomGraph
import DisjointSetList
import BinaryTree


def printCCResults(graph, result):
    print(graph.vertices.keys())
    print(graph.edges)

    for l in result:
        l.print()
def printTreeResults (result):
    for r in result.values():
        print(r.toArray())

if __name__ == '__main__':
    n = 5
    rg = RandomGraph(n)

    dsl = DisjointSetList.DisjointSetList()
    result1 = dsl.connectedComponents(rg)

    dsle = DisjointSetList.DisjointSetListHeuristic()
    result2 = dsle.connectedComponents(rg)

    printCCResults(rg, result1)
    printCCResults(rg, result2)

    dst = DisjoinedSetTree.DisjoinedSetTree()
    result3 = dst.connectedComponents(rg)
    print()
    printTreeResults(result3)

