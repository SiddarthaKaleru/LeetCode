class Solution(object):
    def checkDivisibility(self, n):
        def ds(x):
            ans=0
            while x>0:
                ans+=x%10
                x//=10
            return ans
        def dp(x):
            ans=1
            while x>0:
                ans*=x%10
                x//=10
            return ans
        return n%(ds(n)+dp(n))==0