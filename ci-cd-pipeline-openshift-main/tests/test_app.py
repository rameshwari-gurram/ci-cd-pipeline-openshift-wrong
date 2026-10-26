"""Unit tests for the sample application."""

import unittest

from app import add_numbers, greet


class TestApplication(unittest.TestCase):
    """Test application functions."""

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_greet_strips_whitespace(self):
        self.assertEqual(greet(" Vaidehi "), "Hello, Vaidehi!")

    def test_greet_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            greet("   ")


if __name__ == "__main__":
    unittest.main()
