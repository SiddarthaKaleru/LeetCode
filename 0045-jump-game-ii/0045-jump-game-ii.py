class Solution(object):
    def jump(self, nums):
        n=len(nums)
        i=0
        reach=last=jump=0
        while last<n-1:
            reach=max(reach,i+nums[i])
            if i==last:
                last=reach
                jump+=1
            i+=1
        return jump