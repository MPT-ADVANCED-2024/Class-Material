"""
We will never use the operation to increase two different types of resources. This is because if we were to increase two different types of resources, they would cancel each other out and none of them would be increased.

Therefore, we will only use the operation to increase at most one type of resources.

If there are more than one type of resources that is below the desired amount, then we cannot balance the resources.

Otherwise, we can calculate how much we need to increase the resource to reach the desired amount, and check if we have enough other types of resources to decrease.
"""


def solve() -> bool:
    N = int(input())
    a = [int(v) for v in input().split()]
    b = [int(v) for v in input().split()]
    cost = 0
    for x, y in zip(a, b):
        if x < y:
            if cost:
                return False
            cost = y - x
    for x, y in zip(a, b):
        if x >= y and x - y < cost:
            return False
    return True


for _ in range(int(input())):
    print("YES" if solve() else "NO")


"""
3
4
0 10 9 1
1 9 8 0
3
2 2 3
3 3 2
2
1 10
5 5
"""

"""
YES
NO
YES
"""
