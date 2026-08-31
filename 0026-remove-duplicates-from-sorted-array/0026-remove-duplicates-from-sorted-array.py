class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        ind=0
        for i in range(1,n):
            if nums[ind]!=nums[i]:
                nums[ind+1]=nums[i]
                ind+=1
        return ind+1