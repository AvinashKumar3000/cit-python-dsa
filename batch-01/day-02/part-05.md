# prob LC_744 find smallest letter

```python
class Solution:
    def nextGreatestLetter(self, letters, target):
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]
```
