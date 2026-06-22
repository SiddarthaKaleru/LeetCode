class Solution(object):
    def lengthOfLongestSubstring(self, s):
        map={}
        l=0
        n=len(s)
        ml=0
        for r in range(n):
            if s[r] not in map or map[s[r]]<l:
                ml=max(ml,r-l+1)
            else:
                l=map[s[r]]+1
            map[s[r]]=r
        return ml