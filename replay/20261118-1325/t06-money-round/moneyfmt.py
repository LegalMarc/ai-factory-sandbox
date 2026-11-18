"""Decimal rounding helpers for money formatting."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def round_half_up(value, places):
    """Round a decimal number given as text, halves away from zero.

    ``value`` is a string such as ``"3.14159"`` or ``"-2.5"`` and ``places``
    is a non-negative integer.  The result is a string with exactly ``places``
    digits after the decimal point (or no point when ``places`` is 0).
    """
    if not isinstance(places, int) or isinstance(places, bool) or places < 0:
        raise ValueError("places must be a non-negative integer")

    try:
        number = Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("value is not a valid decimal number: {!r}".format(value))

    if not number.is_finite():
        raise ValueError("value is not a valid decimal number: {!r}".format(value))

    quantum = Decimal(1).scaleb(-places)
    rounded = number.quantize(quantum, rounding=ROUND_HALF_UP)

    if rounded == 0:
        rounded = abs(rounded)

    return format(rounded, "f")
