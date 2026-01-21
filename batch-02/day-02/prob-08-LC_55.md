# LC_55 jump game

```python
class Solution:
    def canJump(self, nums):
        max_reach = 0
        n = len(nums)
        for i in range(n):
            next_step = i + nums[i]

            if i > max_reach:
                return False

            max_reach = max(max_reach, next_step )

        return True
```
