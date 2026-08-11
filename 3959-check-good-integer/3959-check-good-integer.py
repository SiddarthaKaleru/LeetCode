class Solution(object):
    def checkGoodInteger(self, n):
        def ds(n):
            ans=0
            while n>0:
                ans+=n%10
                n//=10
            return ans
        def ss(n):
            ans=0
            while n>0:
                ans+=(n%10)**2
                n//=10
            return ans
        return ss(n)-ds(n)>=50