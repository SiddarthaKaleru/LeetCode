class Solution(object):
    def digitFrequencyScore(self, n):
        d=defaultdict(int)
        while n > 0:
            rem = n % 10
            d[rem]+=1
            n //= 10
        ans=0
        for i,j in d.items():
            ans+=i*j
        return ans