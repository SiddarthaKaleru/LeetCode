# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        pa=headA
        pb=headB
        while pa is not pb:
            if pa is None: pa=headB
            else:pa=pa.next
            if pb is None: pb=headA
            else:pb=pb.next
        return pa