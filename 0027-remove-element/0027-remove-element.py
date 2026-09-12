class Solution(object):
    def removeElement(self, nums, val):
        ind=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[ind]=nums[i]
                ind+=1
        return ind