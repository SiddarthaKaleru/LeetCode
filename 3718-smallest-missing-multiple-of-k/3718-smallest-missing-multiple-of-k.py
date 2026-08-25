class Solution(object):
    def missingMultiple(self, nums, k):
        ans=k
        while True:
            if ans not in nums:
                return ans
            ans+=k