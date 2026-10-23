class Solution(object):
    def convert(self, s, numRows):
        if numRows==1 or numRows>=len(s):
            return s
        ans=['']*numRows
        ind,st=0,1
        for x in s:
            ans[ind]+=x
            if ind==0: st=1
            elif ind==numRows-1: st=-1
            ind+=st
        return ''.join(ans)