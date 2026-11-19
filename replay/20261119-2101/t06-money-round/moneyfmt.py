from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext


def round_half_up(value, places):
    if isinstance(places, bool) or not isinstance(places, int):
        raise TypeError("places must be an int")
    if places < 0:
        raise ValueError("places must be 0 or more")
    if not isinstance(value, str):
        raise ValueError("value must be a string representing a number")
    try:
        d = Decimal(value)
    except (InvalidOperation, ValueError) as e:
        raise ValueError(f"invalid decimal value: {value!r}") from e
    if not d.is_finite():
        raise ValueError(f"invalid decimal value: {value!r}")
    quantum = Decimal(1).scaleb(-places)
    prec = max(28, len(value) + places + 10, len(d.as_tuple().digits) + places + 10)
    with localcontext() as ctx:
        ctx.prec = prec
        quantized = d.quantize(quantum, rounding=ROUND_HALF_UP)
    if quantized == 0:
        quantized = quantized.copy_abs()
    return format(quantized, "f")
