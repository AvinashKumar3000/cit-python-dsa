```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -nums[i]

            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return result

```

```python
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i>0 and nums[i-1] == nums[i]:
                continue

            left = i+1
            right = n-1
            x = nums[i]

            while left < right:
                y = nums[left]
                z = nums[right] 

                if y+z == -x:
                    res.append([x,y,z])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                    	left += 1
                    while left < right and nums[right] == nums[right+1]:
                    	right -= 1

                elif y+z < -x:
                	left += 1
                else:
                	right -= 1
                

        return res
```
