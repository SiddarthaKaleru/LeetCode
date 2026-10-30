class Solution(object):
    def findErrorNums(self, nums):
        mpp=set()
        ans=[]
        for i in nums:
            if i in mpp:
                ans.append(i)
                break
            mpp.add(i)
        n=len(nums)
        nsum=(n*(n+1))//2
        s=sum(nums)
        ans.append(nsum-s+ans[0])
        return ans