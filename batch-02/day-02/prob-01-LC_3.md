# LC_3 Longest Substring Without Repeating Characters

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = {}
        max_ln = 0
        left = 0

        for i in range(n):
            right, ch = i, s[i]
            if ch in seen and seen[ch] >= left:
                left = seen[ch]+1
            
            seen[ch] = right
            max_ln = max(max_ln, right - left + 1)
        
        return max_ln
```
