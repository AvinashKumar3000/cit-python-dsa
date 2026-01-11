# easy   - LC_283 move zeros

- using single pointer method
- using swap 
- 

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[i],nums[p] = nums[p],nums[i]
                p += 1
```