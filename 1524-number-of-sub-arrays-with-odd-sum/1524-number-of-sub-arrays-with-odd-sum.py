class Solution(object):
    def numOfSubarrays(self, arr):
        oddCount, prefixSum, mod = 0, 0, 10**9+7
        for a in arr:
            prefixSum += a
            oddCount += prefixSum % 2
        oddCount += (len(arr) - oddCount) * oddCount
        return oddCount % mod