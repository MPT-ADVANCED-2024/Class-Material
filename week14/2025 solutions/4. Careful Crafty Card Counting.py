"""
"do not pick up any two consecutive cards, and do not leave any two consecutive cards on the table"

This requirement tells us that we can either pick up all the even-indexed cards or all the odd-indexed cards.

If we pick up all the even-indexed cards, we choose the greatest common divisor of all the even-indexed cards as K, and check if all the odd-indexed cards are not divisible by K.

The same applies if we pick up all the odd-indexed cards.
"""

from math import gcd


def solve():
    N = int(input())
    a = [int(v) for v in input().split()]
    if N == 1:
        return a[0]

    evens = a[::2]  # [a[0], a[2], a[4], ...]
    odds = a[1::2]  # [a[1], a[3], a[5], ...]

    K = evens[0]
    for x in evens[1:]:
        K = gcd(K, x)
    if all(x % K != 0 for x in odds):
        return K

    K = odds[0]
    for x in odds[1:]:
        K = gcd(K, x)
    if all(x % K != 0 for x in evens):
        return K

    return "UNWINNABLE"


for _ in range(int(input())):
    print(solve())

"""
2
3
83 33 9
3
62 49 82
"""

"""
33
2
"""

"""
2
5
84 89 8 75 72
5
15 63 23 34 92
"""

"""
4
UNWINNABLE
"""
