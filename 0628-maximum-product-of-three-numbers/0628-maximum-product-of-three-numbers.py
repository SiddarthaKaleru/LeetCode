class Solution(object):
    def maximumProduct(self, nums):
        a=heapq.nlargest(3,nums)
        b=heapq.nsmallest(3,nums)
        return max(a[0]*a[1]*a[2], b[0]*b[1]*a[0])