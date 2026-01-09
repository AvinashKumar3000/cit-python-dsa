# prob 01: LC_704 Binary Search

- nums      List[int]   sorted
- target    int

search target
	- return index
	- return -1

```python
class Solution:
    def search(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
```