from hw2 import makeConnected
import unittest
class TestTaskManager(unittest.TestCase):
    def test_visit():
        assert makeConnected(4, [[0,1],[0,2],[1,2]]) == 1
        assert makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]) == 2
        assert makeConnected(5, [[0,1],[0,2],[3,4],[2,3]]) == 0
        assert makeConnected(6, [[0,1],[0,2],[1,2],[3,4],[3,5]]) == -1

unittest.main()
