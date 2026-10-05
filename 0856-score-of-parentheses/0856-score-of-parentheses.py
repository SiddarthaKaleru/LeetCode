class Solution(object):
    def scoreOfParentheses(self, s):
        st,cur=[],0
        for i in s:
            if i=='(':
                st.append(cur)
                cur=0
            else:
                cur+=st.pop()+max(cur,1)
        return cur