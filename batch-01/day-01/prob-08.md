# easy   - LC_387 first unique char in str

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = dict()
        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        n = len(s)
        for i in range(n):
            ch = s[i]
            if freq[ch] == 1:
                return i
        return -1        

```
