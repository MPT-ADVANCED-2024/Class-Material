from typing import NamedTuple


class S(NamedTuple):
    sum: int
    size: int


def op(a: S, b: S) -> S:
    return S(a.sum + b.sum, a.size + b.size)


def e() -> S:
    return S(0, 0)


F = int


def mapping(f: F, x: S) -> S:
    return S(x.sum + f * x.size, x.size)


def composition(f: F, g: F) -> F:
    return f + g


def id() -> F:
    return 0


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
        def _apply(i: int, tl: int, tr: int) -> None:
            if r < tl or tr < l:  # [l, r] and [tl, tr] don't intersect
                return
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
    a = [1, 5, 4, 2, 3]
    seg = LazySegTree([S(x, 1) for x in a])
    print(seg.prod(1, 3))  # 5+4+2=11
    seg.apply(1, 2, 2)  # [1, 5, 4, 2, 3] -> [1, 7, 6, 2, 3]
    print(seg.prod(2, 3))  # 6+2=8
    seg.apply(0, 4, 1)  # [1, 7, 6, 2, 3] -> [2, 8, 7, 3, 4]
    print(seg.prod(0, 3))  # 2+8+7+3=20
