# LC_922 sort array by parity 2

```python
class Solution:
    def sortArrayByParityII(self, nums):
        n = len(nums)
        even = []
        odd = []
        for x in nums:
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        for i in range(n):
            if i%2==0:
                nums[i] = even.pop()
            else:
                nums[i] = odd.pop()
        return nums
```