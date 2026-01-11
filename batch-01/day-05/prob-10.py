# prob-10 LC_39 combinations_sum

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        n = len(candidates)

        def dfs(start, path, total):
            if total == target:
                res.append(path.copy())
            if total > target:
                return
            for i in range(start,n):
                x = candidates[i]
                dfs(i, path+[x] , x + total)
        
        dfs(0,[],0)
        return res