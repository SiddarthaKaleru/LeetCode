class Solution(object):
    def maxNumberOfBalloons(self, text):
        hm=defaultdict(int)
        for i in text:
            hm[i]+=1
        ans=float('inf')
        for i in "ban":
            ans=min(ans,hm[i])
        for i in "lo":
            ans=min(ans,hm[i]//2)
        return ans