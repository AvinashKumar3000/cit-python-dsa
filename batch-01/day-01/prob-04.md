# easy   - LC_217 contains duplicate

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        ln = len(set(nums))
        if ln == n:
            return False
        else:
            return True
```