class Solution(object):
    def isAcronym(self, words, s):
        n=len(words)
        n1=len(s)
        if n!=n1:
            return False
        for i in range(n):
            if words[i][0] != s[i]:
                return False
        return True