import pytest
from calculator import square


def test_zero():
    assert square(0) == 0


def test_positive_numbers():
    assert square(2) == 4
    assert square(3) == 9


def test_negative_numbers():
    assert square(-2) == 4
    assert square(-3) == 9


def test_str():
    with pytest.raises(TypeError):
        square("Cat")
