from fraction import Fraction
import pytest


def test_fraction_initialization():
    # Test valid initialization
    f = Fraction(1, 2)
    assert f.numerator == 1
    assert f.denominator == 2

    # Test invalid initialization with non-integer numerator
    with pytest.raises(TypeError):
        Fraction(1.5, 2)

    # Test invalid initialization with non-integer denominator
    with pytest.raises(TypeError):
        Fraction(1, 2.5)

    # Test invalid initialization with zero denominator
    with pytest.raises(ValueError):
        Fraction(1, 0)

    # Test invalid initialization with negative denominator
    with pytest.raises(ValueError):
        Fraction(1, -2)


def test_fraction_operations():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)

    # Test addition
    assert f1 + f2 == (1 / 2) + (1 / 3)

    # Test subtraction
    assert f1 - f2 == (1 / 2) - (1 / 3)

    # Test multiplication
    assert f1 * f2 == (1 / 2) * (1 / 3)

    # Test division
    assert f1 / f2 == (1 / 2) / (1 / 3)


def test_fraction_comparisons():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    f3 = Fraction(2, 4)

    # Test equality
    assert f1 == f3
    assert f1 != f2

    # Test less than and greater than
    assert f2 < f1
    assert f1 > f2

    # Test less than or equal to and greater than or equal to
    assert f2 <= f1
    assert f1 >= f2


def test_division_by_zero():
    f1 = Fraction(1, 2)
    f_zero = Fraction(0, 1)

    # Test division by a fraction with numerator zero
    with pytest.raises(ZeroDivisionError):
        f1 / f_zero


def test_invalid_operations():
    f1 = Fraction(1, 2)
    not_a_fraction = 5

    # Test addition with non-fraction
    with pytest.raises(TypeError):
        f1 + not_a_fraction

    # Test subtraction with non-fraction
    with pytest.raises(TypeError):
        f1 - not_a_fraction

    # Test multiplication with non-fraction
    with pytest.raises(TypeError):
        f1 * not_a_fraction

    # Test division with non-fraction
    with pytest.raises(TypeError):
        f1 / not_a_fraction


def test_invalid_comparisons():
    f1 = Fraction(1, 2)
    not_a_fraction = 5

    # Test equality comparison with non-fraction
    with pytest.raises(TypeError):
        f1 == not_a_fraction

    # Test inequality comparison with non-fraction
    with pytest.raises(TypeError):
        f1 != not_a_fraction

    # Test less than comparison with non-fraction
    with pytest.raises(TypeError):
        f1 < not_a_fraction

    # Test less than or equal to comparison with non-fraction
    with pytest.raises(TypeError):
        f1 <= not_a_fraction

    # Test greater than comparison with non-fraction
    with pytest.raises(TypeError):
        f1 > not_a_fraction

    # Test greater than or equal to comparison with non-fraction
    with pytest.raises(TypeError):
        f1 >= not_a_fraction
