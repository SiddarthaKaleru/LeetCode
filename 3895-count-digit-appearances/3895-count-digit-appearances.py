class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        ans = 0
        for i in nums:
            n = i
            while n > 0:
                rem = n % 10
                if rem == digit: ans += 1
                n //= 10
        return ans