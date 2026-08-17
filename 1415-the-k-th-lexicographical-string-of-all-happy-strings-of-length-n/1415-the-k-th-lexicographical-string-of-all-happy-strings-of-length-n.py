class Solution(object):
    def getHappyString(self, n, k):
        nl={'a':'bc', 'b':'ac', 'c':'ab'}
        q=collections.deque(['a','b','c'])
        while len(q[0]) != n:
            u=q.popleft()
            for v in nl[u[-1]]:
                q.append(u+v)
        return q[k-1] if len(q)>=k else ''