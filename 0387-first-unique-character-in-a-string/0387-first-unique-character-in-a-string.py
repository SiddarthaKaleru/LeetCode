class Solution(object):
    def firstUniqChar(self, s):
        hm=defaultdict(int)
        ans=len(s)
        for i,v in enumerate(s):
            if v not in hm:
                hm[v]=i
            else:
                hm[v]=-1
        for v in hm.values():
            if v!=-1:
                ans=min(ans,v)
        return ans if ans!=len(s) else -1