from typing import Optional

INF = int(1e9)

S = int


def op(a: int, b: int) -> int:
    return min(a, b)


def e() -> int:
    return INF


F = Optional[int]


def mapping(f: F, s: S) -> S:
    return f if f is not None else s


def composition(f: F, g: F) -> F:
    return f if f is not None else g


def id() -> F:
    return None


"""
d: data
lz: lazy tag
tl, tr: tree left, tree right
l, r: query left, query right
"""


class LazySegTree:
    def __init__(self, arr: list[S]) -> None:
        self._N = len(arr)
        self._d = [e() for _ in range(4 * self._N)]
        self._lz = [id() for _ in range(4 * self._N)]

        def _build(p: int, tl: int, tr: int) -> None:
            if tl == tr:
                self._d[p] = arr[tl]
                return
            m = (tl + tr) // 2
            _build(p * 2, tl, m)
            _build(p * 2 + 1, m + 1, tr)
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
            self._push(p)
            tm = (tl + tr) // 2
            _set(2 * p, tl, tm)
            _set(2 * p + 1, tm + 1, tr)
            self._update(p)

        _set(1, 0, self._N - 1)

    def prod(self, l: int, r: int) -> S:  # [l, r]
        def _prod(i: int, tl: int, tr: int) -> S:
            if r < tl or tr < l:  # [l, r] and [tl, tr] don't intersect
                return e()
            print(f"prod {l=} {r=} range=[{tl}, {tr}]")
            if l <= tl and tr <= r:  # [l, r] includes [tl, tr]
                return self._d[i]
            self._push(i)
            tm = (tl + tr) // 2
            return op(
                _prod(i * 2, tl, tm),
                _prod(i * 2 + 1, tm + 1, tr),
            )

        return _prod(1, 0, self._N - 1)

    def apply(self, l: int, r: int, f: F) -> None:  # [l, r]
        def _apply(i: int, tl: int, tr: int) -> None:  # [l, r]
            if r < tl or tr < l:  # [l, r] and [tl, tr] don't intersect
                return
            print(f"apply {l=} {r=} {f=} range=[{tl}, {tr}]")
            if l <= tl and tr <= r:  # [l, r] includes [tl, tr]
                self._all_apply(i, f)
                return
            self._push(i)
            tm = (tl + tr) // 2
            _apply(i * 2, tl, tm)
            _apply(i * 2 + 1, tm + 1, tr)
            self._update(i)

        return _apply(1, 0, self._N - 1)

    def all_prod(self) -> S:
        return self._d[1]

    def _update(self, i: int) -> None:
        self._d[i] = op(self._d[i * 2], self._d[i * 2 + 1])

    def _all_apply(self, i: int, f: F) -> None:
        self._d[i] = mapping(f, self._d[i])
        self._lz[i] = composition(f, self._lz[i])

    def _push(self, i: int) -> None:
        self._all_apply(i * 2, self._lz[i])
        self._all_apply(i * 2 + 1, self._lz[i])
        self._lz[i] = id()


if __name__ == "__main__":
    a = [18, 17, 13, 19, 15, 11, 20, 99]
    seg = LazySegTree(a)
    print(f"{seg.prod(1, 3)=}\n")  # min(17, 13, 19) = 13
    print(f"{seg.prod(4, 7)=}\n")  # min(15, 11, 20, 99) = 11
    seg.set(5, 77)  # a = [18, 17, 13, 19, 15, 77, 20, 99]
    print(f"{seg.prod(4, 7)=}\n")  # min(15, 77, 20, 99) = 15
    seg.apply(0, 3, 30)  # a = [30, 30, 30, 30, 15, 77, 20, 99]
    seg.set(3, 7)  # a = [30, 30, 30, 7, 15, 77, 20, 99]
