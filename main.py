# TODO IMPLEMENTAZIONE GRAFO
# creiamo prima i grafi per gli n valori e li memorizziamo in modo da non sprecare tempo per la creazione
# TODO CLASSE BASE UNION FIND

# TODO LISTA BASE
# TODO LISTA CON EURISTICA
# TODO ALBERI
from typing import Optional

from RandomGraph import RandomGraph
import DisjointSetList


def printCCResults(graph, result):
    print(graph.vertices.keys())
    print(graph.edges)

    for l in result:
        l.print()


def verifySameResults(result1, result2):
    if len(result1) != len(result2):
        raise (Exception("Total lengths don't match"))
    for i in range (0, len(result1)):
        l1 = result1[i].head
        l2 = result2[i].head
        r1 = r2 = []
        while l1:
            r1.append(l1.val)
            l1 = l1.next
        while l2:
            r2.append(l2.val)
            l2 = l2.next
        if sorted(r1) != sorted(r2):
            raise (Exception("Arrays don't match"))
    print("SAME RESULTS!")


if __name__ == '__main__':
    n = 10
    rg = RandomGraph(n)

    dsl = DisjointSetList.DisjointSetList()
    result1 = dsl.connectedComponents(rg)

    dsle = DisjointSetList.DisjointSetListHeuristic()
    result2 = dsle.connectedComponents(rg)

    printCCResults(rg, result1)
    printCCResults(rg, result2)
    verifySameResults(result1, result2)
