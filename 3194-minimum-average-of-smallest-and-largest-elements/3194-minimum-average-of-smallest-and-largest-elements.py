class Solution(object):
    def minimumAverage(self, nums):
        n=len(nums)
        nums.sort()
        arr=[]
        i,j=0,n-1
        while i<j:
            arr.append(float(nums[i]+nums[j])/2)
            i+=1
            j-=1
        return min(arr)