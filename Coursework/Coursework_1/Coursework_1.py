#!/usr/bin/env python3

def first_n_powers(base, n):
    return [base ** exponent for exponent in range(1, n + 1)]


def a_times_b(a, b=None):
    if b is not None:
        return a * b
    else:
        return a


def first_five_powers_of_base(base):
    if base is None:
        return None
    elif not base:
        return [base - base, base - base, base - base, base - base, base - base]

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
    # Write a script that prints out the first five powers of 2 (2, 4, 8, 16, 32).
    print(first_n_powers(base=2, n=5))

    # Write a script that prints the first five powers of two, but only uses the digit "2", no other digits.
    print(first_five_powers_of_base(base=2))

    # Write a script that prints the first five powers of two, but only uses the digit "3".
    print(first_five_powers_of_base(base=3 - (3 // 3)))

    # Write a script that prints out the first 7 Fibonnaci numbers (1, 1, 2, 3, 5, 8, 13)
    # only using the digit 1. (In the Fibonnaci sequence, each number is the sum of the previous two.)
    print(first_seven_fibonnaci())
