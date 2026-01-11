# LC_503  next greatest ele 2

```python
class Solution:
	def nextGreaterElements(self, nums):
		n = len(nums)
		result = []

		for i in range(n):
			max_val = -1
			for j in range(i+1,i+n):
				idx = j%n
				if nums[idx] > nums[i]:
					max_val = nums[idx]
					break
			result.append(max_val)
		return result
```
