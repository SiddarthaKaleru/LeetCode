class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = ""
        for word in words:
            t=0
            for i in word:
                t += weights[ord(i)-97]
            t %= 26
            t = 26 - t
            c = chr(t+96)
            ans += c
        return ans