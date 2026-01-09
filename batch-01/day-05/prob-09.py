# LC_78
# next prob: LC_90 SUBSET 2

class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)

        def backtrack(start, path):
            res.append(path)
            for i in range(start, n):
                x = nums[i]
                backtrack(i+1,path + [x])

        backtrack(0, [])
        return res