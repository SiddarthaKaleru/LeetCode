class Solution(object):
    def reverse(self, x):
        flag=0
        if x<0:
            flag=1
            x=-x
        temp=x
        rev=0
        while temp:
            rem=temp%10
            rev=rem+rev*10
            temp=temp//10
        if flag==1:
            rev=-rev
        if rev<(-2)**31 or rev>2**31-1:
            return 0
        return rev