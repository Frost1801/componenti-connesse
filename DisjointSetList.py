from typing import Optional

from DisjointSet import DisjointSet
from LinkedList import ListNode, LinkedList, ExtendedLinkedList
from RandomGraph import RandomGraph


# implementazione delle componenti connesse tramite liste collegate con puntatori
class DisjointSetList(DisjointSet):
    # restituisce una lista concatenata il cui unico elemento è x
    def makeSet(self, x: Optional[ListNode]):
        return LinkedList(x)

    def union(self, x: Optional[ListNode], y: Optional[ListNode]):
        y = y.list.head
        x.list.tail.next = y
        x.list.tail = y.list.tail
        while y:
            y.list = x.list
            y = y.next

    def findSet(self, x: Optional[ListNode]):
        return x.list.head

    def connectedComponents(self, g: Optional[RandomGraph]):
        lists = []
        nodes = []
        for i in range(0, g.numVert):
            nodes.append(ListNode(g.vertices[i], None))
            lists.append(self.makeSet(nodes[i]))
        for edge in g.edges.values():
            u = nodes[edge[0]]
            v = nodes[edge[1]]
            self.sameComponent(u, v, lists)
        return lists

    def sameComponent(self, u: Optional[ListNode], v: Optional[ListNode], lists):
        if self.findSet(u) != self.findSet(v):
            lists.remove(v.list)
            self.union(u, v)


class DisjointSetListHeuristic(DisjointSetList):
    def makeSet(self, x: Optional[ListNode]):  # ritorna la lista che ha anche la lunghezza invece che quella normale
        return ExtendedLinkedList(x)

    def sameComponent(self, u: Optional[ListNode], v: Optional[ListNode], lists):
        if self.findSet(u) != self.findSet(v):
            b = u
            s = v
            if u.list.length < v.list.length:  # confronta la lunghezza delle due liste e cambia big e small in base a quella
                b = v
                s = u
            lists.remove(s.list)
            super().union(b, s)
            b.list.length += s.list.length
