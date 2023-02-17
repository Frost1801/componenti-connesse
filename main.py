# TODO IMPLEMENTAZIONE GRAFO
# creiamo prima i grafi per gli n valori e li memorizziamo in modo da non sprecare tempo per la creazione
# TODO CLASSE BASE UNION FIND

# TODO LISTA BASE
# TODO LISTA CON EURISTICA
# TODO ALBERI
# TODO SALVATAGGIO SU FILE CSV

from RandomGraph import RandomGraph
from Tester import Tester


def printCCResults(graph, result):
    print(graph.vertices.keys())
    print(graph.edges)

    for l in result:
        l.print()


def printTreeResults(result):
    for r in result.values():
        print(r.toArray())


if __name__ == '__main__':
    n = 200
    t = Tester(n)
    t.runTests()
