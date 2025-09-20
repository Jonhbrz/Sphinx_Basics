import pytest
from maths.add import add_nums
from maths.subtract import subtract_nums
from maths.multiply import multiply_nums
from maths.divide import divide_nums

def test_add_nums():
    assert add_nums(2, 3, 5) == 10
    assert add_nums(1, 2, 3, 4) == 10
    assert add_nums() == 0  # sin argumentos

def test_subtract_nums():
    assert subtract_nums(100, 20, 30, 40) == 10
    assert subtract_nums(50, 10, 5) == 35
    assert subtract_nums(10) == 10  # solo un argumento
    assert subtract_nums() == 0  # sin argumentos

def test_multiply_nums():
    assert multiply_nums(2, 3, 4) == 24
    assert multiply_nums(1, 5, 2) == 10
    assert multiply_nums() == 1  # sin argumentos

def test_divide_nums():
    assert divide_nums(100, 2, 5) == 10.0
    assert divide_nums(50, 2) == 25.0
    assert divide_nums(10) == 10  # solo un argumento
    with pytest.raises(ValueError):
        divide_nums(10, 0)  # división por cero
    assert divide_nums() is None  # sin argumentos