#TODO IMPLEMENTAZIONE GRAFO
    #creiamo prima i grafi per gli n valori e li memorizziamo in modo da non sprecare tempo per la creazione
#TODO CLASSE BASE UNION FIND

    #TODO LISTA BASE
    #TODO LISTA CON EURISTICA
    #TODO ALBERI


from RandomGraph import RandomGraph
import DisjointSetList

if __name__ == '__main__':
    n = 10
    rg = RandomGraph(n)
    #dsl = DisjointSetList.DisjointSetList()
    dsle = DisjointSetList.DisjointSetListHeuristic()
    # print(rg.vertices.keys())
    # print(rg.edges)
    # result = dsl.connectedComponents(rg)
    # for l in result:
    #    l.print()
    print(rg.vertices.keys())
    print(rg.edges)
    result = dsle.connectedComponents(rg)
    for l in result:
        l.print()