class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        ans=0
        st=set(nums)
        for i in nums:
            if (i+diff) in st and (i+2*diff) in st:
                ans+=1
        return ans