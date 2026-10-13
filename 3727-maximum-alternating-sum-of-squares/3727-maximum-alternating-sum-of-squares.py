class Solution(object):
    def maxAlternatingSum(self, nums):
        arr=[abs(x) for x in nums]
        arr.sort(reverse=True)
        n=len(arr)
        if n%2==0:
            mid=n//2
        else:
            mid=(n//2)+1
        ans=sum(arr[i]**2 for i in range(0,mid))
        ans-=sum(arr[i]**2 for i in range(mid,n))
        return ans
        