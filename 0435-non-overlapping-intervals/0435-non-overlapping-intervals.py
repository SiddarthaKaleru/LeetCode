class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        res = 0
        intervals.sort(key=lambda x:x[1])
        pre = intervals[0][1]

        for i in range(1,len(intervals)):
            if pre > intervals[i][0]:
                res += 1
            else:
                pre = intervals[i][1]
        return res
        