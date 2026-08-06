class Solution(object):
    def smallestNumber(self, n, t):
        def dp(n):
            ans=1
            while n>0:
                ans*=n%10
                n=n//10
            return ans
        while True:
            pn=dp(n)
            if pn%t==0:
                return n
            n+=1