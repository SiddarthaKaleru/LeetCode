class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        set1,set2=set(nums1),set(nums2)
        a,b=0,0
        for i in nums1:
            if i in set2:
                a+=1
        for i in nums2:
            if i in set1:
                b+=1
        return [a,b]