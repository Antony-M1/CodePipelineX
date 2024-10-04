import unittest
from generated_code import bubble_sort


class TestGeneratedCode(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(bubble_sort([5, 3, 8, 4]), [3, 4, 5, 8])


if __name__ == '_main_':
    unittest.main()
