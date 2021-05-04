import calculator


def test_add_method():
    assert 1 == calculator.addition(0, 1)
    assert 1 == calculator.addition(1, 0)
    assert 2 == calculator.addition(0, 2)
    assert 2 == calculator.addition(2, 0)
    assert 2 == calculator.addition(1, 1)
    assert 3 == calculator.addition(1, 2)
    assert 3 == calculator.addition(2, 1)
<<<<<<< HEAD
    assert 3 == calculator.addition(1, 2)
=======
    assert 3 == calculator.addition(2, 1)
>>>>>>> 493be072020cd11614658587b514287773de38d3


def test_subtract_method():
    assert -1 == calculator.subtract(0, 1)
    assert -2 == calculator.subtract(0, 2)
    assert 1 == calculator.subtract(1, 0)
    assert 2 == calculator.subtract(2, 0)
    assert 1 == calculator.subtract(2, 1)
    assert 1 == calculator.subtract(3, 2)
