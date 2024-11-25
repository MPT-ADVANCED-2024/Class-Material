## [Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/)

```python
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        N = len(arr)
        j = N + arr.count(0) - 1
        for i in reversed(range(N)):
            if arr[i] == 0:
                if j < N: arr[j] = 0
                j -= 1
            if j < N: arr[j] = arr[i]
            j -= 1
```
