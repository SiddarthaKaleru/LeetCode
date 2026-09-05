class Solution(object):
    def firstStableIndex(self, nums, k):
        m=-1
        ca,cm=0,0
        for i,x in enumerate(nums):
            m=max(m,x)
            if i==ca: cm=m
            if x<cm-k: ca=i+1
        return ca if ca<len(nums) else -1