from unittest import TestCase
from calculator import Calculator
class TestCalculator(TestCase):

 def test_add(self):
    self.Calculator = Calculator()
    self.assertEqual(self.Calculator.add(3, 4), 7)


 def test_multiply(self):
    self.fail()
