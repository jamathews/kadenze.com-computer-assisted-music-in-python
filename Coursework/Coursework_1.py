#!/usr/bin/env python3

def first_n_powers(base, n):
    return [base ** exponent for exponent in range(1, n + 1)]


def a_times_b(a, b=None):
    if b:
        return a * b
    else:
        return a


def first_five_powers_of_base(base):
    powers_of_base = []
    val = None
    one = base // base
    for i in range(one + one + one + one + one):
        val = a_times_b(a=base, b=val)
        powers_of_base.append(val)

    return powers_of_base


def first_seven_fibonnaci():
    fibonnaci = [1, 1]

    for i in range(1 + 1 + 1 + 1 + 1):
        val = fibonnaci[-1 - 1] + fibonnaci[-1]
        fibonnaci.append(val)

    return fibonnaci


if __name__ == '__main__':
    print(first_n_powers(base=2, n=5))
    print(first_five_powers_of_base(base=2))
    print(first_five_powers_of_base(base=3 - (3 // 3)))
    print(first_seven_fibonnaci())
