# 238. Product of Array Except Self

[go to](https://leetcode.com/problems/product-of-array-except-self/description/)

```python
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1] * n
        right = [1] * n

        lp = 1
        for i in range(n):
            left[i] = lp
            lp *= nums[i]

        rp = 1
        for i in range(n - 1, -1, -1):
            right[i] = rp
            rp *= nums[i]

        res = []
        for i in range(n):
            res.append(left[i] * right[i])

        return res

```
