# LC_45 jump game ||

```python
class Solution:
    def jump(self, nums):
        farthest = 0
        curr_end = 0
        jump = 0 

        n = len(nums)
        for i in range(n-1):
            next_step = i + nums[i]
            farthest = max(farthest, next_step)

            if i==curr_end:
                jump += 1
                curr_end = farthest

        return jump

```
