class Solution(object):
    def findMissingElements(self, nums):
        nums=set(nums)
        mi=min(nums)
        ma=max(nums)
        ans=[]
        for i in range(mi+1,ma):
            if i not in nums:
                ans.append(i)
        return ans