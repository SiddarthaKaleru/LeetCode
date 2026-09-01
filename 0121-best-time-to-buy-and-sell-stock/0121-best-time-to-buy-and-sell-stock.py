class Solution(object):
    def maxProfit(self, prices):
        maxp=0
        minp=10001
        for i in prices:
            if minp>i: minp=i
            if maxp<i-minp: maxp=i-minp
        return maxp