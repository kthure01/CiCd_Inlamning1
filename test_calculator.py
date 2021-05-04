# Importerar funktionerna för kalkylatorn
import calculator


# Denna testmetod kontrollera att additionsmetoden fungerar som den ska.
def test_add_method():
    assert 1 == calculator.addition(0, 1)
    assert 1 == calculator.addition(1, 0)
    assert 2 == calculator.addition(0, 2)
    assert 2 == calculator.addition(2, 0)
    assert 2 == calculator.addition(1, 1)
    assert 3 == calculator.addition(1, 2)
    assert 3 == calculator.addition(2, 1)
    assert 3 == calculator.addition(1, 2)
    assert 3 == calculator.addition(2, 1)


# Denna metod kontrollerar att subtraktionsmetoden fungerar som den ska.
def test_subtract_method():
    assert -1 == calculator.subtract(0, 1)
    assert -2 == calculator.subtract(0, 2)
    assert 1 == calculator.subtract(1, 0)
    assert 2 == calculator.subtract(2, 0)
    assert 1 == calculator.subtract(2, 1)
    assert 1 == calculator.subtract(3, 2)
