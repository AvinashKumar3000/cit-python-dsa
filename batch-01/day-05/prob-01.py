class Solution:
    def combinationSum(self, candidates, target):
            res = []

            def dfs(start, path, total):
                if total == target:
                    res.append(path.copy())
                if total > target:
                    return

                for i in range(start, len(candidates)):
                    dfs(i, path + [candidates[i]], candidates[i] + total)
            dfs(0,[],0)
            return res

