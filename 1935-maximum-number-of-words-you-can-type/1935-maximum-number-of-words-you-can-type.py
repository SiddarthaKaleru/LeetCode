class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        s=text.split()
        broke=set(brokenLetters)
        ans=0
        for w in s:
            for c in w:
                if c in broke:
                    ans+=1
                    break
        return len(s)-ans