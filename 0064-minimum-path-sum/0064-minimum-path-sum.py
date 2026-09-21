class Solution(object):
    def minPathSum(self, nums):
        m,n=len(nums),len(nums[0])
        dp=[[0 for j in range(n)] for i in range(m)]
        dp[0][0]=nums[0][0]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+nums[i][0]
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+nums[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+nums[i][j]
        return dp[m-1][n-1]