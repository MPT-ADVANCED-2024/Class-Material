> Copied from <https://github.com/atcoder/ac-library>

# Segtree

It is the data structure for [monoids](https://en.wikipedia.org/wiki/Monoid) $(S, \cdot: S \times S \to S, e \in S)$, i.e., the algebraic structure that satisfies the following properties.

- associativity: $(a \cdot b) \cdot c$ = $a \cdot (b \cdot c)$ for all $a, b, c \in S$
- existence of the identity element: $a \cdot e$ = $e \cdot a$ = $a$ for all $a \in S$

Given an array $S$ of length $N$, it processes the following queries in $O(\log N)$ time:

- Updating an element
- Calculating the product of the elements of an interval

The following should be defined:

- The type `S`
- The binary operation `S op(S a, S b)`
- The identity element `S e()`

# Lazy Segtree

It is the data structure for the pair of a [monoid](https://en.wikipedia.org/wiki/Monoid) $(S, \cdot: S \times S \to S, e \in S)$ and a set $F$ of $S \to S$ mappings that satisfies the following properties.

- $F$ contains the identity map $\mathrm{id}$, where the identity map is the map that satisfies $\mathrm{id}(x) = x$ for all $x \in S$.
- $F$ is closed under composition, i.e., $f \circ g \in F$ holds for all $f, g \in F$.
- $f(x \cdot y) = f(x) \cdot f(y)$ holds for all $f \in F$ and $x, y \in S$.

Given an array $S$ of length $N$, it processes the following queries in $O(\log N)$ time:

- Applying the map $f\in F$ (cf. $x = f(x)$) on all the elements of an interval
- Calculating the product of the elements of an interval

The following should be defined:

- The type `S` of the monoid
- The binary operation `S op(S a, S b)`
- The function `S e()` that returns $e$
- The type `F` of the map
- The function `S mapping(F f, S x)` that returns $f(x)$
- The function `F composition(F f, F g)` that returns $f \circ g$
- The function `F id()` that returns $\mathrm{id}$
