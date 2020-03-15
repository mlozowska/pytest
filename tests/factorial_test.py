from src.factorial import factorial
import pytest


@pytest.mark.parametrize(
    "n,result",
    [
        (4, 24),
        (0, 1),
        (-10, False),
        ("test", False),
        (1.5, False)
    ]
)
def test_factorial(n, result):
    assert factorial(n) == result
