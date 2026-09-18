class Solution(object):
    def combine(self, n, k):
        res=[]
        def dfs(st,path):
            if len(path)==k:
                res.append(path)
                return
            for i in range(st,n+1):
                dfs(i+1,path+[i])
        dfs(1,[])
        return res