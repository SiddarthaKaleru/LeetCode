class Solution(object):
    def longestPalindrome(self, s):
        best=1
        l1=[0,0]
        n=len(s)
        for i in range(n):
            l,r=i,i
            while r<n-1 and s[l]==s[r+1]:
                r+=1
            while l>-1 and r<n and s[l]==s[r]:
                if r-l+1>best:
                    best=r-l+1
                    l1=[l,r]
                l-=1
                r+=1
        return s[l1[0]:l1[1]+1]