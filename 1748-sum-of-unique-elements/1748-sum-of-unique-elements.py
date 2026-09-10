class Solution(object):
    def sumOfUnique(self, nums):
        ans=0
        n=len(nums)
        hm=defaultdict(int)
        for i in nums:
            hm[i]+=1
        for i,j in hm.items():
            if j==1:
                ans+=i
        return ans