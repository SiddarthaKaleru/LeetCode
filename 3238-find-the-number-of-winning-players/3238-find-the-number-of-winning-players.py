class Solution(object):
    def winningPlayerCount(self, n, pick):
        a={}
        for i,j in pick:
            if (i,j) not in a:
                a[(i,j)]=0
            a[(i,j)]+=1
        c=0
        for i in range(n):
            for (p,co),j in a.items():
                if p==i and j>i:
                    c+=1
                    break
        return c