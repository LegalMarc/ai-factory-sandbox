import re
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation, localcontext

_VALID = re.compile(r"^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$")


def round_half_up(value, places):
    if isinstance(places, bool) or not isinstance(places, int):
        raise ValueError("places must be an int of 0 or more")
    if places < 0:
        raise ValueError("places must be an int of 0 or more")
    if not isinstance(value, str) or not _VALID.match(value):
        raise ValueError(f"invalid number: {value!r}")
    try:
        number = Decimal(value)
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"invalid number: {value!r}") from exc
    if not number.is_finite():
        raise ValueError(f"invalid number: {value!r}")
    quant = Decimal(1).scaleb(-places)
    with localcontext() as ctx:
        ctx.prec = max(50, len(value) + places + 10, len(number.as_tuple().digits) + places + 10)
        rounded = number.quantize(quant, rounding=ROUND_HALF_UP)
    if rounded.is_zero():
        rounded = rounded.copy_abs()
    return format(rounded, "f")
