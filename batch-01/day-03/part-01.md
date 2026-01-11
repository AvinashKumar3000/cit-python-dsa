# LC_496  next greatest ele  

```python
class Solution:
	def nextGreaterElement(self, nums1, nums2):
		n1 = len(nums1)
		n2 = len(nums2)
		result = []
		for i in range(n1):
			max_val = -1
			is_found = False
			for j in range(n2):
				if nums1[i] == nums2[j]:
					is_found = True
				if is_found and nums2[j] > nums1[i]:
					max_val = nums2[j]
					break
			result.append(max_val)
		return result
```
