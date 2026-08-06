class Solution(object):
    def minimumPushes(self, word):
        n=len(word)
        if n<=8: return n
        elif n<=16:
            t=n-8
            return 8+t*2
        elif n<=24:
            if n==24: return 48
            t=n%8
            return 24+t*3
        elif n==25: return 52
        elif n==26: return 56