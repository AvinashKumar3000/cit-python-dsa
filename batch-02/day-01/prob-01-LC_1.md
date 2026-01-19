# LC_1 two sum

[go to](https://leetcode.com/problems/two-sum/)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        n = len(nums)
        for i in range(n):
            x = nums[i]
            other = target - x
            if other in hm:
                return [hm[other], i]
            hm[x] = i
        return []
```
