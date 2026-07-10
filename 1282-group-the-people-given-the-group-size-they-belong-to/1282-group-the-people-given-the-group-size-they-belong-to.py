class Solution(object):
    def groupThePeople(self, groupSizes):
        d = defaultdict(list)
        n = len(groupSizes)
        for i, val in enumerate(groupSizes):
            if val in d:
                arr = d[val]
                arr.append(i)
                d[val] = arr
            else:
                arr = [i]
                d[val] = arr
        ans=[]
        for size, arr in d.items():
            for i in range(0,len(arr),size):
                ans.append(arr[i:i+size])
        return ans