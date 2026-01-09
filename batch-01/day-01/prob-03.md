# easy   - LC_268 missing number

nums ->  [ 0, n ]

5    ->  0 1 3 4 5

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        original = (n*(n+1))//2
        actual = sum(nums)
        return original - actual

```
