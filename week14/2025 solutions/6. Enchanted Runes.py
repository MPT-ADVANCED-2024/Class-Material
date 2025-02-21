"""
To handle the updates, we can use a segment tree. We can store the minimum and maximum values of `(a[i] - i)` and `(a[i] + i)` for each segment, and the maximum potency within a segment can be calculated from the two children segments.
"""

from dataclasses import dataclass

INF = int(1e17)


@dataclass
class S:  # The monoid
    sub_min: int  # minimum value of a[i] - i within the segment
    add_min: int  # minimum value of a[i] + i within the segment
    sub_max: int  # maximum value of a[i] - i within the segment
    add_max: int  # maximum value of a[i] + i within the segment
    ans: int  # maximum potency within the segment

    @classmethod
    def from_value(cls, i: int, x: int) -> "S":
        return cls(
            sub_min=x - i,
            add_min=x + i,
            sub_max=x - i,
            add_max=x + i,
            ans=0,
        )


def op(lhs: S, rhs: S) -> S:  # the binary operation satisfying the monoid laws
    return S(
        sub_min=min(lhs.sub_min, rhs.sub_min),
        add_min=min(lhs.add_min, rhs.add_min),
        sub_max=max(lhs.sub_max, rhs.sub_max),
        add_max=max(lhs.add_max, rhs.add_max),
        ans=max(
            lhs.ans,
            rhs.ans,
            rhs.sub_max - lhs.sub_min,  # (a[r] - r) - (a[l] - l)
            lhs.add_max - rhs.add_min,  # (a[l] + l) - (a[r] + r)
        ),
    )


def e() -> S:  # the identity element
    return S(
        sub_min=INF,
        add_min=INF,
        sub_max=-INF,
        add_max=-INF,
        ans=0,
    )


class SegTree:
    def __init__(self, arr: list[S]) -> None:
        self._N = len(arr)
        self._d = [e() for _ in range(4 * self._N)]

        def _build(p: int, tl: int, tr: int) -> None:
            if tl == tr:
                self._d[p] = arr[tl]
                return
            tm = (tl + tr) // 2
            _build(2 * p, tl, tm)
            _build(2 * p + 1, tm + 1, tr)
            self._update(p)

        _build(1, 0, self._N - 1)

    def set(self, i: int, x: S) -> None:
        def _set(p, tl, tr):
            if i < tl or tr < i:
                return
            if tl == tr:
                self._d[p] = x
                return
            tm = (tl + tr) // 2
            _set(2 * p, tl, tm)
            _set(2 * p + 1, tm + 1, tr)
            self._update(p)

        _set(1, 0, self._N - 1)

    def all_prod(self) -> S:
        return self._d[1]

    def _update(self, p: int) -> None:
        self._d[p] = op(self._d[2 * p], self._d[2 * p + 1])


def solve():
    N, Q = map(int, input().split())
    a = [S.from_value(i, int(x)) for i, x in enumerate(input().split())]
    seg = SegTree(a)
    print(seg.all_prod().ans, end=" ")
    for _ in range(Q):
        i, x = map(int, input().split())
        seg.set(i - 1, S.from_value(i - 1, x))
        print(seg.all_prod().ans, end=" ")
    print()


for _ in range(int(input())):
    solve()

"""
4
2 2
2 8
1 8
2 1
5 3
2 3 4 5 6
3 8
1 5
5 3
8 6
8 6 1 3 2 1 5 4
5 3
1 9
3 3
8 13
7 1
3 1
5 0
1 4 6 8 4
"""

"""
5 0 6
0 4 4 4
5 5 6 4 10 11 11
4
"""
