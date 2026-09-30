class Solution(object):
    def maxDepthAfterSplit(self, seq):
        groups = []
        d = 0
        for c in seq:
            open = c == '('
            if open:
                d += 1
            groups.append(d % 2)
            if not open:
                d -=1
        return groups