from src.calculator import Calculator
import pytest

calc = Calculator()


@pytest.mark.parametrize(
    "x,y,result",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, -2, -3)
    ]
)
def test_add(x, y, result):
    assert calc.add(x, y) == result


@pytest.mark.parametrize(
    "x,y,result",
    [
        (1, 2, -1),
        (0, 0, 0),
        (-1, -2, 1)
    ]
)
def test_sub(x, y, result):
    assert calc.sub(x, y) == result
