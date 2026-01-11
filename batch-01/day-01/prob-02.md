# easy   - LC_136 single number

- linear runtime complexity -> O(n)
- constant extra space      -> O(1)

## XOR technique

x = x^n

where if you do xor of same number twice.
it will get cancelled.

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for x in nums[1:]:
            res = res ^ x
        return res
```