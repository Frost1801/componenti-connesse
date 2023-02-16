from typing import Optional

from DisjointSet import DisjointSet
from RandomGraph import RandomGraph

#rappresenta un nodo della lista

class ListNode:
    def __init__(self, data: Optional[chr], nextNode):
        self.val = data
        self.next = nextNode
        self.list = None  #mantiene il valore del set object (LinkedList) del nodo


class LinkedList:  # set object
    def __init__(self, node: Optional[ListNode]):
        self.head = node
        self.tail = node
        node.list = self  #aggiorna il valore del set object del nodo

    #stampa la lista
    def print(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next
        print()

class ExtendedLinkedList (LinkedList):
    def __init__(self, node: Optional[ListNode]):
        super().__init__(node)
        self.length = 1 #siccome la lista inizia con un singolo elemento, la lunghezza è inizializzata ad 1





