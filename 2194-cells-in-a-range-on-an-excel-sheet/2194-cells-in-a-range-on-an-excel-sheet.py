class Solution(object):
    def cellsInRange(self, s):
        ans=[]
        for c in range(ord(s[0]),ord(s[3])+1):
            for r in range(ord(s[1]),ord(s[4])+1):
                ans.append(chr(c)+chr(r))
        return ans