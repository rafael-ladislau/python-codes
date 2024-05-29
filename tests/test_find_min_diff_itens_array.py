import unittest

from src.find_min_diff_itens_array import quicksort, find_min_diff

class TestFunctions(unittest.TestCase):

    # Tests for quicksort
    def test_quicksort_empty(self):
        self.assertEqual(quicksort([]), [])

    def test_quicksort_single_element(self):
        self.assertEqual(quicksort([1]), [1])

    def test_quicksort_multiple_elements(self):
        self.assertEqual(quicksort([3, 1, 2]), [1, 2, 3])

    def test_quicksort_duplicates(self):
        self.assertEqual(quicksort([3, 1, 2, 2]), [1, 2, 2, 3])

    def test_quicksort_already_sorted(self):
        self.assertEqual(quicksort([1, 2, 3]), [1, 2, 3])

    # Tests for find_min_diff
    def test_find_min_diff_multiple_elements(self):
        self.assertEqual(find_min_diff([1, 20, 10, 23, 50]), 3)

    def test_find_min_diff_two_elements(self):
        self.assertEqual(find_min_diff([10, 20]), 10)

    def test_find_min_diff_duplicates(self):
        self.assertEqual(find_min_diff([3, 1, 2, 2]), 0)

    def test_find_min_diff_negative_numbers(self):
        self.assertEqual(find_min_diff([-10, -20, -30]), 10)

    def test_find_min_diff_single_element(self):
        self.assertIsNone(find_min_diff([1]))

    def test_find_min_diff_empty(self):
        self.assertIsNone(find_min_diff([]))

if __name__ == '__main__':
    unittest.main()