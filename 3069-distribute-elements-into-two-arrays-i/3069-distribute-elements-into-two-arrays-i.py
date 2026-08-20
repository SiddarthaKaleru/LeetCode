class Solution(object):
    def resultArray(self, nums):
        ans=([nums[0]],[nums[1]])
        for x in nums[2:]:
            ans[ans[0][-1]<=ans[1][-1]].append(x)
        return ans[0]+ans[1]