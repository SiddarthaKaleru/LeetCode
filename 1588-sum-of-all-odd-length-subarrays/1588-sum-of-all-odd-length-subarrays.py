class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n=len(arr)
        ans=0
        for i,a in enumerate(arr):
            l,r=i,n-i-1
            ans+=a*(l//2+1)*(r//2+1)
            ans+=a*((l+1)//2)*((r+1)//2)
        return ans