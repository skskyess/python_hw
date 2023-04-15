from hw import visit
import unittest

class TestTaskManager(unittest.TestCase):
    def test_visit():
        assert visit([[1], [2], [3], []]) == True

        assert visit([[1, 3], [3, 0, 1], [2], [0]]) == False

        assert visit([[1, 2, 3]]) == True

        assert visit([[]]) == True

unittest.main()
