class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans=1
        g=math.gcd(a,b)
        for i in range(2,g+1):
            ans+=a%i==0 and b%i==0
        return ans