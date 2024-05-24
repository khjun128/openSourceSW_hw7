import unittest.mock

from func import add_func, equal_func, hello_func


class TestFunc(unittest.TestCase):
    @unittest.mock.patch("func.hello_func")
    def test_hello_func(self, mock_hello_func):
        mock_hello_func.return_value = "Hello world"
        self.assertEqual(hello_func("world"), "Hello world")

    @unittest.mock.patch("func.equal_func")
    def test_equal_func(self, mock_equal_func):
        mock_equal_func.side_effect = lambda a, b: a == b
        self.assertTrue(equal_func(1, 1))
        self.assertFalse(equal_func(1, 2))

    @unittest.mock.patch("func.add_func")
    def test_add_func(self, mock_add_func):
        mock_add_func.side_effect = lambda a, b: a + b
        self.assertEqual(add_func(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
