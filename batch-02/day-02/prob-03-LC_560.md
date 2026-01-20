# LC_560 Subarray Sum Equals K

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sum = {}
        prefix_sum[0] = 1

        for num in nums:
            curr_sum += num

            need = curr_sum - k
            if need in prefix_sum:
                count += prefix_sum[need]
            
            if curr_sum in prefix_sum:
                prefix_sum[curr_sum] += 1
            else:
                prefix_sum[curr_sum] = 1

        return count
```
