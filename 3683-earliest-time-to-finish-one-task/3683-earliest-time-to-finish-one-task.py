class Solution(object):
    def earliestTime(self, tasks):
        ans=201
        for i in tasks:
            ans=min(ans,i[0]+i[1])
        return ans