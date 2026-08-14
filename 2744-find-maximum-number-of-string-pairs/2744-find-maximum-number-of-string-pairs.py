class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        s=set()
        ans=0
        for w in words:
            if w in s:
                ans+=1
            else:
                s.add(w[::-1])
        return ans