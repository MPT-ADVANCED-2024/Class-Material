# [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt_zero = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt_zero += 1
            while cnt_zero > k:
                if nums[l] == 0:
                    cnt_zero -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
```
