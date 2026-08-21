class Solution(object):
    def makeSmallestPalindrome(self, s):
        n=len(s)
        ans=""
        for i in range(n):
            ans+=min(s[i],s[n-i-1])
        return ans