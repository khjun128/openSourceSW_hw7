import unittest

from func import add_func, equal_func, hello_func


class TestFunc(unittest.TestCase):
    def test_hello_func(self):
        self.assertEqual(hello_func("world"), "Hello world")

    def test_equal_func(self):
        self.assertTrue(equal_func(1, 1))
        self.assertFalse(equal_func(1, 2))

    def test_add_func(self):
        self.assertEqual(add_func(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
