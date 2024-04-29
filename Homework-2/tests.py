import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):

    def test1(self):

        contrived_func(0)

    def test2(self):

        contrived_func(-1)

    def test3(self):

        contrived_func(7)

    def test4(self):

        contrived_func(10)

    def test5(self):

        contrived_func(11)

    def test6(self):

        contrived_func(100)

    def test7(self):

        contrived_func(-8)

    def test8(self):

        contrived_func(21)


if __name__ == '__main__':
    unittest.main()
