class Solution(object):
    def divideArray(self, nums):
        hm=defaultdict(int)
        for i in nums:
            hm[i]+=1
        for i in hm.values():
            if i%2!=0:
                return False
        return True