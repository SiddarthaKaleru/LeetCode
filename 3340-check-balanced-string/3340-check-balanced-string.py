class Solution(object):
    def isBalanced(self, num):
        n=len(num)
        s1,s2=0,0
        for i in range(0,n,2):
            s1+=int(num[i])
        for i in range(1,n,2):
            s2+=int(num[i])
        return s1 == s2