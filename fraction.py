class Fraction:
    def __init__(self, numerator: int, denominator: int):
        """Initialize a Fraction instance and validate the input."""
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")
        self.numerator = numerator
        if denominator <= 0:
            raise ValueError("Denominator must be positive.")
        self.denominator = denominator

    def __str__(self):
        """Return a string representation of the fraction."""
        return f"The fraction has numerator {self.numerator}, and denominator {self.denominator}. The fraction equals {self.numerator / self.denominator}"

    def __repr__(self):
        """Return a string representation of the fraction for debugging."""
        return f"Fraction(numerator={self.numerator}, denominator={self.denominator})"

    def __eq__(self, other):
        """Check if two fractions are equal."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction objects.")
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other):
        """Check if two fractions are not equal."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction objects.")
        return self.numerator * other.denominator != self.denominator * other.numerator

    def __lt__(self, other):
        """Check if one fraction is less than another."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction objects.")
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other):
        """Check if one fraction is less than or equal to another."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction objects.")
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other):
        """Check if one fraction is greater than another."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction objects.")
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other):
        """Check if one fraction is greater than or equal to another."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction objects.")
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __add__(self, other):
        """Add two fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only add Fraction objects.")
        return (self.numerator / self.denominator) + (
            other.numerator / other.denominator
        )

    def __sub__(self, other):
        """Subtract one fraction from another."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only subtract Fraction objects.")
        return (self.numerator / self.denominator) - (
            other.numerator / other.denominator
        )

    def __mul__(self, other):
        """Multiply two fractions."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only multiply Fraction objects.")
        return (self.numerator / self.denominator) * (
            other.numerator / other.denominator
        )

    def __truediv__(self, other):
        """Divide one fraction by another."""
        if not isinstance(other, Fraction):
            raise TypeError("Can only divide Fraction objects.")
        if other.numerator == 0:
            raise ZeroDivisionError(
                "Cannot divide by a fraction with a numerator of zero."
            )
        return (self.numerator / self.denominator) / (
            other.numerator / other.denominator
        )
