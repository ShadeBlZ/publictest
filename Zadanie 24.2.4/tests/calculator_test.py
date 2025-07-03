import pytest

from app.calculator import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_adding_succes(self):
        assert self.calc.adding(self,1,1) == 2

    def test_subtraction_succes(self):
        assert self.calc.subtraction(self,5,3) == 2


    def test_multiply_succes(self):
        assert self.calc.multiply(self,4,4) == 16

    def test_division_succes(self):
        assert self.calc.division(self,10,5) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)

    def teardown(self):
        print('Выполнение метода Teardown')


