# LC_77 combinations

from itertools import combinations
class Solution:
    def combine(self, n,k):
        nums = [ i+1 for i in range(n)]
        return list(combinations(nums,k))