# LC_78
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