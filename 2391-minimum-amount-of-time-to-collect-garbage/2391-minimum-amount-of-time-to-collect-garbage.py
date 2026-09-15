class Solution(object):
    def garbageCollection(self, garbage, travel):
        last={}
        res=0
        n=len(garbage)
        for i in range(n):
            res+=len(garbage[i])
            for c in garbage[i]:
                last[c]=i
        for j in range(1,len(travel)):
            travel[j]+=travel[j-1]
        for c in 'PGM':
            if last.get(c,0):
                res+=travel[last[c]-1]
        return res