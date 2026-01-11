# PRob 12 LC_216 combinations sum 3

## solution 1

from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        digits = list(range(1, 10))
        for comb in combinations(digits, k):
            if sum(comb) == n:
                res.append(list(comb))
        return res

## solution 2

class Solution:
    def combinationSum3(self, k, n):
        res = []
        target = n
        nums = list(range(1,10))

        def dfs(start, path, total):
            if total == target and len(path) == k:
                res.append(path.copy())
            if total > target and len(path) > k:
                return

            for i in range(start, len(nums)):
                x = nums[i]
                dfs(i+1, path + [x], x+total)
        dfs(0,[],0)
        return res
        