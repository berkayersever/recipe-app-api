from django.test import TestCase
from app.calculator import add


class CalculatorTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(2, 3), 5)
