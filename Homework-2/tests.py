import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):

    def test1(self):

        contrived_func(3)

    def test2(self):

        contrived_func(-3)

    def test3(self):

        contrived_func(100)

    def test4(self):

        contrived_func(1)

    def test5(self):

        contrived_func(11)

    def test6(self):

        contrived_func(6)

    def test7(self):

        contrived_func(7)

    def test8(self):

        contrived_func(10)


if __name__ == '__main__':
    unittest.main()
