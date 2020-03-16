from django.test import TestCase
from app.calculator import add, subtract


class CalculatorTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(2, 3), 5)

    def test_subtract_numbers(self):
        """Test that values are subtracted from each other"""
        self.assertEqual(subtract(5, 8), 3)
