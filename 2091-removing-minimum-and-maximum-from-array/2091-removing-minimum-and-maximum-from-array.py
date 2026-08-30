class Solution(object):
    def minimumDeletions(self, nums):
        n=len(nums)
        i,j=nums.index(min(nums)),nums.index(max(nums))
        return min(max(i+1,j+1),max(n-i,n-j),i+1+n-j,j+1+n-i)