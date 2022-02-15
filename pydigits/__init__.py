# coding=utf-8

from mpmath import mp
from typing_extensions import Literal

def pi_digits(decimals: int) -> int:
    if type(decimals) != int:
        raise TypeError('"decimals" must be an integer')
    decimals += 1
    mp.dps = decimals
    return mp.pi

def sum_pi_digits(decimals: int,
                  nature: Literal['all', 'even', 'odd']='all',
                  notation: Literal['decimal', 'binary']='decimal'
                  ) -> int:
    pi = pi_digits(decimals)
    decimals += 1
    string_pi = str(pi)

    counter = 0
    dicc = {'odd': 1, 'even': 0, 'all': 2}
    if nature not in dicc:
        raise TypeError('"nature" must be "all", "even" or "odd"')

    for i in range(len(string_pi)):
        if i > 1:
            aux = int(string_pi[i])
            if nature == 'all' or aux % 2 == dicc[nature]:
                counter += aux
    if notation == 'decimal':
        return counter
    elif notation == 'binary':
        return int(bin(counter)[2::])
    else:
        raise TypeError('"notation" must be "decimal" or "binary"')
