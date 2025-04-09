from calculator import Calculator

def test_caiculator():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_calculator():
    calculator = Calculator()
    res = calculator.sum(-6,-10)
    assert res == -16

def test_caiculator2():
    calculator = Calculator()
    res = calculator.sum(-6,6)
    assert res == 0

def test_caiculator3():
    calculator = Calculator()
    res = calculator.sum(5.6,4.3)
    res = round(res,1)
    assert res == 9.9

def test_caiculator4():
    calculator = Calculator()
    res = calculator.sum(10,0)
    assert res == 10

def test_caiculator5():
    calculator = Calculator()
    res = calculator.div(10,2)
    assert res == 5

def test_caiculator6():
    calculator = Calculator()
    try:
        calculator.div(10,0)
    except ArithmeticError as err:
        assert str(err) == "На ноль делить нельзя"

def test_caiculator7():
    calculator = Calculator()
    numbers=[]
    res = calculator.avg(numbers)
    assert res == 0

def test_caiculator8():
    calculator = Calculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res = calculator.avg(numbers)
    assert res == 5
