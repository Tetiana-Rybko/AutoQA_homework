from calculator import Calculator
import pytest


@pytest.fixture
def calculator():
    return Calculator()

def test_sum_positive_numbers(calculator):
 assert calculator.sum(4, 5) == 9

def test_subtract_positive_numbers(calculator):
    assert calculator.sub(-6,-10)==-16
def test_division(calculator):

 assert calculator.div(10, 2) == 5

def test_avg_empty_list(calculator):
     assert calculator.avg([]) == 0
def test_avg_list(calculator):
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
 assert calculator.avg(numbers) == 5


