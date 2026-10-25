class Solution(object):
    def countKeyChanges(self, s):
        s=s.lower()
        n=len(s)
        ans=0
        for i in range(n-1):
            if s[i]!=s[i+1]:
                ans+=1
        return ans