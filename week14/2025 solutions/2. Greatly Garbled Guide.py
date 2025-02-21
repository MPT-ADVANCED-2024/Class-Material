"""
Enumerate all possible substrings of length 10 and check if it is a valid date
"""

DAY_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def check_valid(s: str) -> bool:
    if not s[2] == s[5] == "-":
        return False
    for i in range(10):
        if i == 2 or i == 5:
            continue
        if not s[i].isdigit():
            return False
    dd = int(s[:2])
    mm = int(s[3:5])
    yyyy = int(s[6:10])
    if not 2025 <= yyyy < 2028:
        return False
    if not 1 <= mm <= 12:
        return False
    if not 1 <= dd <= DAY_IN_MONTH[mm - 1]:
        return False
    if yyyy == 2025 and (mm < 2 or (mm == 2 and dd <= 15)):
        return False
    return True


def solve():
    N = int(input())
    s = input()
    for start in range(N - 9):
        if check_valid(cur := s[start : start + 10]):
            return cur


print(solve())

"""
26
2025-01-01-01-2025-02-2026
"""

"25-02-2026"

"""
45
1-11-2004--0210230-9214-01-01-2028-12-04-2027
"""

"12-04-2027"
