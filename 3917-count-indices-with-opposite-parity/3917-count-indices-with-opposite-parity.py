class Solution(object):
    def countOppositeParity(self, nums):
        n=len(nums)
        odd=0
        even=0
        ans=[0]*n
        for i in range(n-1,-1,-1):
            if nums[i]%2==1:
                ans[i]=even
                odd+=1
            else:
                ans[i]=odd
                even+=1
        return ans