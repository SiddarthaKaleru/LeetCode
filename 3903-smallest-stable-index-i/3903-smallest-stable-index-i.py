class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)
        for i in range(n):
            t=max(nums[0:i+1])-min(nums[i:n+1])
            if t<=k:
                return i
        return -1