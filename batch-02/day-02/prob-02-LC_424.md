# LC_424 Longest Repeating Character Replacement

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_count = 0
        max_len = 0

        n = len(s)
        for i in range(n):
            right, ch = i, s[i]
            count[ch] = count.get(ch,0) + 1
            max_count = max(max_count, count[ch])

            # sliding
            while (right - left + 1) - max_count > k:
                left_ch = s[left]
                count[left_char] -= 1
                left += 1
            
            max_len = max(max_len, right -left + 1)
        return max_len
```
