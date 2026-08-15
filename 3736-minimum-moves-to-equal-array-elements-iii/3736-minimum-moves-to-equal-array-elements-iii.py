class Solution(object):
    def minMoves(self, nums):
        m=max(nums)
        n=len(nums)
        ans=0
        for i in nums:
            ans+=(m-i)
        return ans