INF = int(1e9)

S = int


def op(a: S, b: S) -> S:
    return min(a, b)


def e() -> S:
    return INF


"""
d: data
tl, tr: tree left, tree right
l, r: query left, query right
"""


class SegTree:
    def __init__(self, arr: list[S]) -> None:
        self._N = len(arr)
        self._d = [e()] * (4 * self._N)  # 2**(ceil(log2(N)) + 1) <= 4 * N

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
        def _set(p: int, tl: int, tr: int) -> None:
            if i < tl or i > tr:
                return
            print(f"set {i=} {x=} range=[{tl}, {tr}]")
            if tl == tr:
                self._d[p] = x
                return
            tm = (tl + tr) // 2
            _set(2 * p, tl, tm)
            _set(2 * p + 1, tm + 1, tr)
            self._update(p)

        _set(1, 0, self._N - 1)

    def prod(self, l: int, r: int) -> S:
        def _prod(p: int, tl: int, tr: int) -> S:
            if r < tl or l > tr:
                return e()
            print(f"prod {l=} {r=} range=[{tl}, {tr}]")
            if l <= tl and tr <= r:
                return self._d[p]
            tm = (tl + tr) // 2
            return op(
                _prod(2 * p, tl, tm),
                _prod(2 * p + 1, tm + 1, tr),
            )

        return _prod(1, 0, self._N - 1)

    def all_prod(self) -> S:
        return self._d[1]

    def _update(self, p: int) -> None:
        self._d[p] = op(self._d[2 * p], self._d[2 * p + 1])


if __name__ == "__main__":
    a = [18, 17, 13, 19, 15, 11, 20, 99]
    seg = SegTree(a)
    print(f"{seg.prod(1, 3)=}\n")  # min(17, 13, 19) = 13
    print(f"{seg.prod(4, 7)=}\n")  # min(15, 11, 20, 99) = 11
    seg.set(5, 77)  # a = [18, 17, 13, 19, 15, 77, 20, 99]
    print(f"{seg.prod(4, 7)=}\n")  # min(15, 77, 20, 99) = 15
