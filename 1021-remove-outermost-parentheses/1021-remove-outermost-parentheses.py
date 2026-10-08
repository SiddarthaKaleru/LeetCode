class Solution(object):
    def removeOuterParentheses(self, s):
        res,opened="",0
        for c in s:
            if c=='(' and opened>0: res+=c
            if c==')' and opened>1: res+=c
            if c=='(':opened+=1 
            else: opened-=1
        return res