# prob LC_33 search in rotated sorted array

```python
class Solution:
    def search(self, nums, target):
        n = len(nums)
        lft = 0
        rht = n-1

        while lft <= rht:
            mid = (lft+rht)//2
            if nums[mid] == target:
                return mid
            if nums[lft] <= nums[mid]:
                # left side sorted
                if target in range(nums[lft],nums[mid]):
                    rht = mid - 1
                else:
                    lft = mid + 1
            else:
                # right side sorted
                if target in range(nums[mid], nums[rht]+1):
                    lft = mid + 1
                else:
                    rht = mid - 1
        return -1
```
