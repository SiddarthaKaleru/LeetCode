class Solution(object):
    def countAsterisks(self, s):
        arr=s.split("|")
        ans=0
        for i in range(len(arr)):
            if i%2==0:
                ans+=arr[i].count("*")
        return ans