from math import isclose


class Temperature:
    def __init__(self, value: float, unit: str = "C"):
        """Initialize a Temperature instance and validate the input."""
        unit = unit.upper()

        if unit not in ("C", "F", "K"):
            raise ValueError("Not a valid unit, Use 'C', 'F' or 'K'")

        self._value = float(value)
        self._unit = unit

        if self.to_kelvin() < 0:
            raise ValueError("Temperature cannot be below absolute zero")

    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Return the temperature unit."""
        return self._unit

    def to_celsius(self) -> float:
        """Convert the temperature to Celsius."""
        if self.unit == "C":
            return self.value
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9
        elif self.unit == "K":
            return self.value - 273.15

    def to_fahrenheit(self) -> float:
        """Convert the temperature to Fahrenheit."""
        if self.unit == "C":
            return (self.value * 9 / 5) + 32
        elif self.unit == "F":
            return self.value
        elif self.unit == "K":
            return ((self.value - 273.15) * 9 / 5) + 32

    def to_kelvin(self) -> float:
        """Convert the temperature to Kelvin."""
        if self.unit == "C":
            return self.value + 273.15
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9 + 273.15
        elif self.unit == "K":
            return self.value

    def convert_to(self, target_unit: str) -> Temperature:
        """Convert the temperature to the specified unit."""
        target_unit = target_unit.upper()

        if target_unit not in ("C", "F", "K"):
            raise ValueError("Not a valid unit, Use 'C', 'F' or 'K'")

        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")
        elif target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")
        else:
            return Temperature(self.to_kelvin(), "K")

    def __repr__(self) -> str:
        """Return a string representation of the temperature."""
        return f"Temperature({self.value}, '{self.unit}')"

    def __str__(self) -> str:
        """Return a string representation of the temperature."""
        return f"{self.value:.2f} °{self.unit}"

    def __eq__(self, other: Temperature) -> bool:
        """Check if two Temperature instances are equal. (==)"""
        if not isinstance(other, Temperature):
            return NotImplemented

        return isclose(self.to_kelvin(), other.to_kelvin(), abs_tol=1e-9)

    def __ne__(self, other: Temperature) -> bool:
        """Check if two Temperature instances are not equal. (!=)"""
        if not isinstance(other, Temperature):
            return NotImplemented

        return not self.__eq__(other)

    def __lt__(self, other: Temperature) -> bool:
        """Check if one Temperature instance is less than another. (<)"""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() < other.to_kelvin()

    def __le__(self, other: Temperature) -> bool:
        """Check if one Temperature instance is less than or equal to another. (<=)"""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() <= other.to_kelvin()

    def __gt__(self, other: Temperature) -> bool:
        """Check if one Temperature instance is greater than another. (>)"""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() > other.to_kelvin()

    def __ge__(self, other: Temperature) -> bool:
        """Check if one Temperature instance is greater than or equal to another. (>=)"""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() >= other.to_kelvin()
