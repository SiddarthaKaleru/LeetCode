class Solution(object):
    def findGCD(self, nums):
        def gcd(a,b):
            while b != 0:
                a, b = b, a % b
            return a
        mi,mx=min(nums),max(nums)
        return gcd(mi,mx)