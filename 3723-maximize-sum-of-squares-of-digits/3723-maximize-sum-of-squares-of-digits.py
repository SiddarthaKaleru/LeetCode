class Solution(object):
    def maxSumOfSquares(self, num, sum):
        ans=""
        if num*9<sum:
            return ""
        for i in range(num):
            if sum>9:
                ans+="9"
                sum-=9
            elif sum>0:
                ans+=str(sum)
                sum=0
            else:
                ans+="0"
        return ans