class Solution(object):
    def minCosts(self, cost):
        n=len(cost)
        for i in range(1,n):
            if cost[i-1]<cost[i]:
                cost[i]=cost[i-1]
        return cost