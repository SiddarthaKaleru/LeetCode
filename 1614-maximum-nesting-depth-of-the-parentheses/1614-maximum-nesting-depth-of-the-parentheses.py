class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        ma=0
        st=[]
        for i in s:
            if i=='(':
                m+=1
                ma=max(m,ma)
            elif i==')': m-=1
        return ma