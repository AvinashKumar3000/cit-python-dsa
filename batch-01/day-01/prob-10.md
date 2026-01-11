# medium - LC_189 rotate array

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        i = (n-k)%n
        res = []
        for _ in range(n):
            res.append(nums[i])
            i = (i+1)%n
        for i in range(n):
            nums[i] = res[i]
```
