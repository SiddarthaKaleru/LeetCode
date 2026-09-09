class Solution(object):
    def countCommas(self, n):
        if n<1000: return 0
        ans=0
        for i in range(1,6):
            ans+=max(0,n-(1000**i)+1)
        return ans