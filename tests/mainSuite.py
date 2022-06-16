import unittest
from Main import main


def broken_function():
    raise Exception('This is broken')


class TestBubleSort(unittest.TestCase):
    def test_sorted(self):
        expected = [11, 28, 28, 33, 43, 45, 48, 52, 57, 61, 71, 71, 74, 74, 77, 82, 93, 93, 96, 98]
        x = main.Arr([74, 28, 48, 77, 11, 93, 96, 52, 74, 45, 28, 98, 57, 82, 93, 61, 43, 71, 71, 33]).bubleSort()
        self.assertEqual(expected, x)

    def test_nil(self):
        expected = []
        x = main.Arr([]).bubleSort()
        self.assertEqual(expected, x)

    def test_all_elem_same(self):
        expected = [1, 1, 1, 1, 1, 1]
        x = main.Arr([1, 1, 1, 1, 1, 1]).bubleSort()
        self.assertEqual(expected, x)

    def test_with_string_inside(self):
        with self.assertRaises(TypeError):
            x = main.Arr([4, 2, 5, 'a', 1]).bubleSort()

    def test_string_only(self):
        expected = ['a', 'b', 'c', 'd']
        actual = main.Arr(['d', 'c', 'a', 'b']).bubleSort()
        self.assertEqual(expected, actual)

    def test_string_with_non_alphabet_inside(self):
        expected = ['e', 'f', 'l', 'qwe']
        actual = main.Arr(['qwe', 'f', 'e', 'l']).bubleSort()
        self.assertEqual(expected, actual)
