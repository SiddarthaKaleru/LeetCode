class Solution(object):
    def longestCommonPrefix(self, strs):
        n=len(strs)
        if n==0: return ""
        strs=sorted(strs)
        st=strs[0]
        last=strs[-1]
        ans=""
        for i in range(min(len(st),len(last))):
            if st[i]!=last[i]:
                return ans
            ans+=st[i]
        return ans