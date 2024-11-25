## [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        acc = 0  # accumulator
        ans = len(nums)  # answer
        for r in range(len(nums)):
            acc += nums[r]
            while acc - nums[l] >= target:
                acc -= nums[l]
                l += 1
            if acc >= target:
                ans = min(ans, r - l + 1)
        return ans if acc >= target else 0
```
