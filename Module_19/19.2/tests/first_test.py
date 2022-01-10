import pytest

from calculator import Calculator

class Testcalc:
    def setup(self):
        self.calc = Calculator

    def test_multiplay_calculate(self):
        assert self.calc.multiply(self, 2, 2) == 4
        
    def test_division_calculate(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calculate(self):
        assert self.calc.subtraction(self, 20, 10) == 10

    def test_adding_calculate(self):
        assert self.calc.adding(self, 50, 40) == 90