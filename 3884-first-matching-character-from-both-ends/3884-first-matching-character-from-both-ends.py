class Solution(object):
    def firstMatchingIndex(self, s):
        n=len(s)
        i,j=0,n-1
        while i<=j:
            if s[i]==s[j]:
                return i
            i+=1
            j-=1
        return -1