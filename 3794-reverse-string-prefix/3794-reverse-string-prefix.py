class Solution(object):
    def reversePrefix(self, s, k):
        if k == 1:
            return s
        if k == len(s):
            return s[::-1]
        sr = s[0:k]
        return sr[::-1] + s[k:]