class Solution(object):
    def maximumOddBinaryNumber(self, s):
        n=len(s)
        ans=""
        o=s.count("1")
        z=n-o
        for i in range(o-1):
            ans+="1"
        for i in range(z):
            ans+="0"
        ans+="1"
        return ans