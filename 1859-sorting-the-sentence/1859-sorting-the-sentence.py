class Solution(object):
    def sortSentence(self, s):
        words=s.split()
        ans=[""]*len(words)
        for word in words:
            i=int(word[-1])-1
            ans[i]=word[:-1]
        return " ".join(ans)