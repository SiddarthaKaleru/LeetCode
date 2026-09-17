class Solution(object):
    def isValid(self, s):
        st=[]
        for i in s:
            if i=='(' or i=='[' or i=="{": st.append(i)
            else:
                if len(st)==0: return False
                elif (st[-1]=='(' and i==')') or (st[-1]=='[' and i==']') or (st[-1]=='{' and i=='}'):
                    st.pop()
                else: return False
        return not len(st)