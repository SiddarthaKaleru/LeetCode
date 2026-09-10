# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.cnt=0

    def calsubtree(self,node):
        if node is None:
            return 0,0
        l=self.calsubtree(node.left)
        r=self.calsubtree(node.right)
        s=l[0]+r[0]+node.val
        n=l[1]+r[1]+1
        if s//n == node.val:
            self.cnt+=1
        return s,n

    def averageOfSubtree(self, root):
        self.calsubtree(root)
        return self.cnt