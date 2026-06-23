class Solution(object):
    def removeStars(self, s):
        st=[]
        for i in range(len(s)):
            if s[i] != '*':
                st.append(s[i])
            else:
                st.pop()
        return ''.join(st)