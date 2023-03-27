from abc import ABC, abstractmethod
from typing import Optional

from RandomGraph import RandomGraph


# classe astratta per avere la stessa interfaccia con le tre possibili implemetnazioni
class DisjointSet(ABC):
    @abstractmethod
    def makeSet(self, x):  # crea un nuovo insieme il cui unico elemento è x
        pass

    @abstractmethod
    def union(self, x, y):  # crea un nuovo insieme composto dall'unione degli insiemi di x e y
        pass

    @abstractmethod
    def findSet(self, x): # restituisce il rappresentante dell'insieme di x
        pass

    @abstractmethod
    def connectedComponents(self, g: Optional[RandomGraph]):
        pass
