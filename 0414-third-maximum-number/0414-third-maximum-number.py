class Solution(object):
    def thirdMax(self, nums):
        m1=float('-inf')
        m2=float('-inf')
        m3=float('-inf')
        for i in nums:
            if i>m1:
                m3=m2
                m2=m1
                m1=i
            elif i>m2 and i != m1:
                m3=m2
                m2=i
            elif i>m3 and i != m1 and i != m2:
                m3=i
        if m3 != float('-inf'):
            return m3
        else: return m1