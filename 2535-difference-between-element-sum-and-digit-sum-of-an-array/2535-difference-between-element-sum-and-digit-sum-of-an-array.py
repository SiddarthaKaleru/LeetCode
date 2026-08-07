class Solution(object):
    def differenceOfSum(self, nums):
        def ds(n):
            ans=0
            while n>0:
                ans+=n%10
                n=n//10
            return ans
        ans1=0
        ans2=0
        for i in nums:
            ans1+=i
            ans2+=ds(i)
        return abs(ans1-ans2)