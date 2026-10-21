class Solution(object):
    def trap(self, height):
        n=len(height)
        pre=[-1]*n
        suf=[-1]*n
        ma=-1
        for i in range(n):
            if ma<height[i]:
                ma=height[i]
            pre[i]=ma
        ma=-1
        for i in range(n-1,-1,-1):
            if ma<height[i]:
                ma=height[i]
            suf[i]=ma
        ans=0
        for i in range(n):
            ans+=min(pre[i],suf[i])-height[i]
        return ans