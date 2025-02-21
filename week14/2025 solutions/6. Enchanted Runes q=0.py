"""
`potency = max(a[l], a[l+1], ..., a[r]) - min(a[l], a[l+1], ..., a[r]) - (r - l)`

We claim that the optimal contiguous sequence having the maximum potency must have the maximum and minimum value at the two ends of the sequence.

(Suppose this is not the case; then we can narrow the sequence (from the side where the extreme element is neither the minimum nor the maximum), and the answer will improve since the length will decrease, while the minimum and maximum will remain unchanged. e.g. `[5, 1, 10, 4, 3]` can be improved to `[1, 10]` with the same minimum and maximum.)

Let's denote the optimal sequence as `a[l], a[l+1], ..., a[r]`, where the minimum or maximum values of `a` lies at `a[l]` or `a[r]`.

There are two cases to consider:
1. a[l] <= a[r], then the maximum potency can be transformed to
    `(a[r] - a[l]) - (r - l) = (a[r] - r) - (a[l] - l)`
2. a[l] > a[r], then the maximum potency can be transformed to
    `(a[l] - a[r]) - (r - l) = (a[l] + l) - (a[r] + r)`

For the first 40% of the tests, there are no changes in values of array a, so we can simply enumerate all possible endpoints of the sequence.

For the first case, we enumerate the right endpoint `(a[r] - r)` of the sequence from left to right, and keep track of the minimum value of `(a[l] - l)` for all `l <= r` to get the maximum potency.

For the second case, we enumerate the left endpoint `(a[l] + l)` of the sequence from right to left, and keep track of the minimum value of `(a[r] + r)` for all `r >= l` to get the maximum potency.
"""

INF = int(1e17)


def solve():
    N, Q = map(int, input().split())
    a = [int(v) for v in input().split()]
    for _ in range(Q):  # ignore updates
        input()
    ans = 0
    cur = INF
    for i in range(N):
        cur = min(cur, a[i] - i)
        if i > 0:
            ans = max(ans, a[i] - i - cur)
    cur = INF
    for i in reversed(range(N)):
        cur = min(cur, a[i] + i)
        if i + 1 < N:
            ans = max(ans, a[i] + i - cur)
    print(ans)


for _ in range(int(input())):
    solve()


"""
4
2 0
2 8
5 0
2 3 4 5 6
8 0
8 6 1 3 2 1 5 4
5 0
1 4 6 8 4
"""

"""
5
0
5
4
"""
