from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def round_half_up(value, places):
    if not isinstance(places, int) or isinstance(places, bool) or places < 0:
        raise ValueError("places must be a non-negative integer")

    try:
        number = Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("value must be a number written as text")

    if not number.is_finite():
        raise ValueError("value must be a finite number")

    quantum = Decimal(1).scaleb(-places)
    rounded = number.quantize(quantum, rounding=ROUND_HALF_UP)
    if rounded == 0:
        rounded = abs(rounded)

    return format(rounded, "f")
