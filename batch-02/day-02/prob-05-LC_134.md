# LC_134 Jump Game

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0
        start_index = 0
        n = len(gas)
        for i in range(n):
            usage = gas[i] - cost[i]
            total_tank += usage
            curr_tank += usage
            if curr_tank < 0:
                curr_tank = 0
                start_index = i+1

        if total_tank >= 0:
            return start_index
        return -1
```
