from typing import Optional

from DisjointSet import DisjointSet
from RandomGraph import RandomGraph


class ListNode:
    def __init__(self, data: Optional[chr], nextNode):
        self.val = data
        self.next = nextNode
        self.list = None


class LinkedList:  # set object
    def __init__(self, node: Optional[ListNode]):
        self.head = node
        self.tail = node
        node.list = self

    def print(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next
        print()


class DisjointSetList(DisjointSet):
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
            if self.findSet(u) != self.findSet(v):
                lists.remove(v.list)
                self.union(u, v)
        return lists

