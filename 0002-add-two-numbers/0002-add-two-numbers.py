# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp=dummy=ListNode(0)
        c=0
        while (l1 is not None or l2 is not None) or c:
            s=0
            if l1 is not None:
                s+=l1.val
                l1=l1.next
            if l2 is not None:
                s+=l2.val
                l2=l2.next
            s+=c
            c=s//10
            s=s%10
            node=ListNode(s)
            temp.next=node
            temp=temp.next
        return dummy.next