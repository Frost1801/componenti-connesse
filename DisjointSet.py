from abc import ABC, abstractmethod
from typing import Optional

from RandomGraph import RandomGraph

#classe astratta per avere la stessa interfaccia con le tre possibili implemetnazioni
class DisjointSet(ABC):
    @abstractmethod
    def makeSet(self, x):
        pass

    @abstractmethod
    def union(self, x, y):
        pass

    @abstractmethod
    def findSet(self, x):
        pass

    @abstractmethod
    def connectedComponents(self, g: Optional[RandomGraph]):
        pass
