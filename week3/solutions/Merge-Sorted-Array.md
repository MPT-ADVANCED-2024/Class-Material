# [Merge Sorted Array](https://leetcode.com/problems/Merge-Sorted-Array/)

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = n - 1
        k = m + n - 1
        for i in reversed(range(m)):
            while j >= 0 and nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            nums1[k] = nums1[i]
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```
