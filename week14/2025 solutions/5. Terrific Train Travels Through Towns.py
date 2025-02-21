"""
For each type of train track, we can build a DSU (or UFDS) to maintain the towns that are connected by that type of train track.

Since there are at most 750 types of train tracks and 100 queries, 750*100 = 75000 is a reasonable complexity for our solution.
"""

from collections import defaultdict


class DSU:
    def __init__(self, N: int) -> None:
        self.fa_or_sz = [-1] * N

    def leader(self, x: int) -> int:
        t = x
        while self.fa_or_sz[t] >= 0:
            t = self.fa_or_sz[t]
        while x != t:
            u = self.fa_or_sz[x]
            self.fa_or_sz[x] = t
            x = u
        return x

    def union(self, x: int, y: int) -> None:
        lx, ly = self.leader(x), self.leader(y)
        if lx == ly:
            return
        if -self.fa_or_sz[lx] < -self.fa_or_sz[ly]:
            lx, ly = ly, lx
        self.fa_or_sz[lx] += self.fa_or_sz[ly]
        self.fa_or_sz[ly] = lx

    def same(self, x: int, y: int) -> bool:
        return self.leader(x) == self.leader(y)


N, M = map(int, input().split())
G = [[] for _ in range(N)]
dsus = defaultdict(lambda: DSU(N))
for _ in range(M):
    u, v, w = map(int, input().split())
    dsus[w].union(u, v)
dsus = list(dsus.values())


def solve():
    s, t = map(int, input().split())
    return sum(dsu.same(s, t) for dsu in dsus)


C = int(input())
for _ in range(C):
    print(solve())


"""
2 3
0 1 0
0 1 2
0 1 2
1
1 0
"""

"""
2
"""

"""
5 8
0 3 0
2 3 3
0 2 0
0 3 0
1 3 2
2 3 1
1 3 2
0 2 2
2
1 3
0 1
"""

"""
1
0
"""
