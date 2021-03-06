from mpmath import mp, ctx_mp_python
from typing_extensions import Literal


def pi_digits(decimals: int) -> ctx_mp_python.numbers:
    if type(decimals) != int:
        raise TypeError('"decimals" must be an integer')
    decimals += 1
    mp.dps = decimals
    return mp.pi


def sum_pi_digits(
    decimals: int,
    nature: Literal["all", "even", "odd"] = "all",
    notation: Literal["decimal", "binary"] = "decimal",
) -> int:
    pi = pi_digits(decimals)
    decimals += 1

    dicc = {"odd": 1, "even": 0, "all": 2}
    if nature not in dicc:
        raise TypeError('"nature" must be "all", "even" or "odd"')

    counter = 0
    for i, character in enumerate(str(pi)):
        if i > 1:
            aux = int(character)
            if nature == "all" or aux % 2 == dicc[nature]:
                counter += aux

    if notation == "decimal":
        return counter
    elif notation == "binary":
        return int(bin(counter)[2::])
    else:
        raise TypeError('"notation" must be "decimal" or "binary"')
