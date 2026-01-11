# LC_74 search a 2d matrix

- matrix
- non - decreasing order

```python
class Solution:
	def searchMatrix(self, matrix, target):
		r = len(matrix)
		c = len(matrix[0])
		n = r * c
		lft = 0
		rht = n-1 
		while lft <= rht:
			mid = ( lft + rht )//2
			curr = matrix[ mid//c ][mid%c]
			if curr == target:
				return True
			if target < curr:
				rht = mid - 1
			else:
				lft = mid + 1

		return False
```
