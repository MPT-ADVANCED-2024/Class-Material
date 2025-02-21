"""
brute force all possible palindromes by inserting a character at every possible position
"""


def solve():
    s = input()
    N = len(s)
    for i in range(N + 1):
        for c in range(ord("a"), ord("z") + 1):
            t = s[:i] + chr(c) + s[i:]
            if t == t[::-1]:
                return t
    return "NONE"


for _ in range(int(input())):
    print(solve())

"""
4
noon
not
statsy
racecar
"""
