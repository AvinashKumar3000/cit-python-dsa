```python
class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        
        for x in nums:
            if x not in freq:
                freq[x] = 0
            freq[x] += 1
        
        fl = [] # frequency list
        for num in freq:
            fl.append((num, freq[num]))
        
        # sort based on count.
        n = len(fl)
        for i in range(n):
            for j in range(i+1, n):
                if fl[i][1] < fl[j][1]:
                    fl[i],fl[j] = fl[j],fl[i]

        res = []
        for i in range(k):
            res.append(fl[i][0])
        
        return res
```