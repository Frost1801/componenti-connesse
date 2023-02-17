from typing import Optional


class Node:  # rappresenta un nodo dell'albero binario di ricerca
    def __init__(self, key):  # costruttore della classe
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.tree = None
        # left e right sono dichiarati e inizializzati a null


class BinaryTree:
    def __init__(self):
        self.root = None

    # metodo per inserire un valore nell'albero
    def insert(self, node: Optional[Node]):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.p = y
        if y is None:
            self.root = node
            node.p = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        node.tree = self

    def toArray(self):
        arr = []
        self._toArray(self.root, arr)
        return arr

    def _toArray(self, node, arr):
        if node:
            self._toArray(node.left, arr)
            arr.append(node.key)
            self._toArray(node.right, arr)
