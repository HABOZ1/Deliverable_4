import pytest
from temperature import Temperature


def test_default_unit():
    """Test that the default unit is Kelvin when not specified."""
    t = Temperature(25)
    assert t.unit == "K"


def test_case_insensitive_unit():
    """Test that the unit is case-insensitive and converted to uppercase."""
    t = Temperature(25, "c")
    assert t.unit == "C"

    t = Temperature(25, "f")
    assert t.unit == "F"

    t = Temperature(25, "k")
    assert t.unit == "K"


def test_read_only_value_and_unit():
    """Test that the value and unit properties are read-only."""
    t = Temperature(25, "C")

    with pytest.raises(AttributeError):
        t.value = 30

    with pytest.raises(AttributeError):
        t.unit = "F"


def test_invalid_unit():
    """Test that an invalid unit raises a ValueError."""
    with pytest.raises(ValueError):
        Temperature(25, "X")


def test_below_absolute_zero():
    """Test that temperatures below absolute zero raise a ValueError."""
    with pytest.raises(ValueError):
        Temperature(-300, "C")

    with pytest.raises(ValueError):
        Temperature(-500, "F")

    with pytest.raises(ValueError):
        Temperature(-10, "K")


def test_absolute_zero():
    """Test that absolute zero is valid."""
    t = Temperature(0, "K")

    assert t.to_celsius() == pytest.approx(-273.15)
    assert t.to_fahrenheit() == pytest.approx(-459.67)


def test_crossover():
    """Test the crossover point where Celsius and Fahrenheit are equal."""
    t = Temperature(-40, "C")

    assert t.to_fahrenheit() == pytest.approx(-40)


def test_frezing_point():
    """Test the freezing point of water."""
    t = Temperature(0, "C")

    assert t.to_fahrenheit() == pytest.approx(32)
    assert t.to_kelvin() == pytest.approx(273.15)


def test_human_body_temperature():
    """Test the average human body temperature."""
    t = Temperature(37, "C")

    assert t.to_fahrenheit() == pytest.approx(98.6)
    assert t.to_kelvin() == pytest.approx(310.15)


def test_boiling_point():
    """Test the boiling point of water."""
    t = Temperature(100, "C")

    assert t.to_fahrenheit() == pytest.approx(212)
    assert t.to_kelvin() == pytest.approx(373.15)


def test_roundtrip_conversion():
    """Test that converting to another unit and back returns the original temperature."""
    t = Temperature(25, "C")

    converted = t.convert_to("F").convert_to("K").convert_to("C")

    assert t == converted


def test_cross_unit_equality():
    """Test that temperatures in different units can be equal."""
    assert Temperature(0, "C") == Temperature(32, "F")


def test_cross_unit_inequality():
    """Test that temperatures in different units can be unequal."""
    assert Temperature(100, "C") != Temperature(100, "F")


def test_cross_unit_less_than():
    """Test that temperatures in different units can be compared."""
    assert Temperature(0, "C") < Temperature(100, "C")


def test_cross_unit_greater_than():
    """Test that temperatures in different units can be compared."""
    assert Temperature(100, "C") > Temperature(273.15, "K")


def test_cross_unit_less_than_or_equal():
    """Test that temperatures in different units can be compared."""
    assert Temperature(0, "C") <= Temperature(32, "F")


def test_cross_unit_greater_than_or_equal():
    """Test that temperatures in different units can be compared."""
    assert Temperature(273.15, "K") >= Temperature(0, "C")


def test_str():
    """Test the string representation of the temperature"""
    t = Temperature(25, "C")
    assert str(t) == "25.00 °C"


def test_repr():
    """Test the repr representation of the temperature"""
    t = Temperature(25, "C")
    assert repr(t) == "Temperature(25.0, 'C')"
