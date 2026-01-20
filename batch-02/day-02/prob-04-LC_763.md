# LC_763 Partition Labels

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {}

        for i,ch in enumerate(s):
            last_pos[ch] = i
        
        partition = []
        left = 0
        right = 0

        for i in range(len(s)):
            right = max(right, last_pos[s[i]])

            if i==right:
                partition.append(right - left + 1)
                left = i + 1

        return partition
```
