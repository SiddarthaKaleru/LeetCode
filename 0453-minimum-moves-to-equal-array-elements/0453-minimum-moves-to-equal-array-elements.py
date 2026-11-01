class Solution(object):
    def minMoves(self, nums):
        mi=nums[0]
        for n in nums:
            mi=min(mi,n)
        res=0
        for n in nums:
            res+=n-mi
        return res