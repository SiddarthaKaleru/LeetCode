class Solution(object):
    def minOperations(self, nums):
        ans=0
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]>=nums[i]:
                ans+=(nums[i-1]+1)-nums[i]
                nums[i]=nums[i-1]+1
        return ans