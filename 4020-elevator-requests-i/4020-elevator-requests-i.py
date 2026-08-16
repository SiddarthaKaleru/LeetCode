class Solution(object):
    def elevatorRequests(self, n, requests):
        ans=requests[0]
        n=len(requests)
        for i in range(1,n):
            ans+=abs(requests[i-1]-requests[i])
        return ans