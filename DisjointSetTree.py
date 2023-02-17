from typing import Optional

import numpy as np

from BinaryTree import BinaryTree, Node
from DisjointSet import DisjointSet
from RandomGraph import RandomGraph


class DisjointSetTree(DisjointSet):
    def makeSet(self, x: Optional[Node]):
        t = BinaryTree()
        t.insert(x)
        return t

    def findSet(self, x: Optional[Node]):
        while x != x.p:
            x = x.p
        return x

    def union(self, x, y):
        while y != y.p:
            y = y.p
        self.findSet(x).tree.insert(y)

    def connectedComponents(self, g: Optional[RandomGraph]):
        trees = {}
        nodes = {}
        vals = list(g.vertices)
        np.random.shuffle(vals)
        for i in range(0, g.numVert):
            nodes[vals[i]] = Node(vals[i])
            trees[nodes[vals[i]]] = (self.makeSet(nodes[vals[i]]))  # mappa per ogni nodo il suo albero
        for edge in g.edges.values():
            u = nodes[edge[0]]
            v = nodes[edge[1]]
            if self.findSet(u) != self.findSet(v):
                trees.pop(self.findSet(v))
                self.union(u, v)
        return trees


class DisjointSetTreePathCompr(DisjointSetTree):
    def findSet(self, x: Optional[Node]):
        if x != x.p:
            x.p = self.findSet(x.p)
        return x.p
