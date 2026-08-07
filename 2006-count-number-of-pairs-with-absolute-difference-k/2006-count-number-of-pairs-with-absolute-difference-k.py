class Solution(object):
    def countKDifference(self, nums, k):
        d={}
        ans=0
        for i in nums:
            ans += d.get(i - k, 0)
            ans += d.get(i + k, 0)
            d[i] = d.get(i, 0) + 1
        return ans