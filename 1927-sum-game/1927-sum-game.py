class Solution(object):
    def sumGame(self, num):
        n=len(num)
        ans=0.0
        for i in range(n):
            if i<n//2:
                sign=1
            else:
                sign=-1
            if num[i]=='?':
                val=4.5
            else:
                val=int(num[i])
            ans+=sign*val
        return ans!=0