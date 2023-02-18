from RandomGraph import RandomGraph
from Tester import Tester
if __name__ == '__main__':
    g = RandomGraph(10)
    n = 400
    t = Tester(n)
    t.runTests()
