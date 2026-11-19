from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext


def round_half_up(value, places):
    if not isinstance(places, int) or isinstance(places, bool) or places < 0:
        raise ValueError("places must be a non-negative integer")

    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("value must be a decimal number") from None

    if not number.is_finite():
        raise ValueError("value must be a finite decimal number")

    digits = len(number.as_tuple().digits)
    precision = max(28, number.adjusted() + places + 3, digits + places + 3)
    quantum = Decimal(1).scaleb(-places)

    with localcontext() as context:
        context.prec = precision
        rounded = number.quantize(quantum, rounding=ROUND_HALF_UP)

    if rounded == 0:
        rounded = abs(rounded)

    return format(rounded, "f")
