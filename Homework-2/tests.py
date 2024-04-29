import unittest
from contrived_func import contrived_func

class TestContrivedFunc(unittest.testcase):

    def test1(self):

        self.assertTrue(contrived_func(3))

    def test2(self):

        self.assertTrue(contrived_func(-3))

    def test3(self):

        self.assertTrue(contrived_func(100))

    def test4(self):

        self.assertTrue(contrived_func(11))


if __name__ == '__main__':
    unittest.main()
