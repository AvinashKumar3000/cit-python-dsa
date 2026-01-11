# LC_905 sort array by parity

```python
class Solution:
    def sortArrayByParity(self, nums):
        n = len(nums)
        l = 0
        r = n-1

        while l <= r:
            if nums[l]%2!=0:
                nums[l],nums[r] = nums[r],nums[l]
                r -= 1
            else:   
                l += 1

        return nums
```
