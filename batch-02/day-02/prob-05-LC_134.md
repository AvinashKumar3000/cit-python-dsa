# LC_134 gas station

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0     # overall petrol balance
        curr_tank = 0      # petrol in current journey
        start_index = 0    # candidate starting station

        for i in range(len(gas)):
            usage = gas[i] - cost[i]
            total_tank += usage
            curr_tank += usage

            # if we fail at station i
            if curr_tank < 0:
                # cannot start from any station before i
                start_index = i + 1
                curr_tank = 0

        # final feasibility check
        if total_tank >= 0:
            return start_index
        return -1
```


```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        start = 0   
        tank = 0
        for i in range(n):
            print(f"{tank} = {tank} + {gas[i]} - {cost[i]} = ", end=" ")
            tank = tank + gas[i] - cost[i]
            print(tank)
            if tank < 0: # cannot start
                start = i + 1
                tank = 0
        
        return start
```
