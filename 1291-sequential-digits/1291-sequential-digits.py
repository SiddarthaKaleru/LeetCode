class Solution(object):
    def sequentialDigits(self, low, high):
        ans = []
        for i in range(1,10):
            num = i
            next = i+1
            while num <= high and next <= 9:
                num = num * 10 + next
                if low <= num and num <= high:
                    ans.append(num)
                next += 1
        ans.sort()
        return ans