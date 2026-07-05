# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        s=[True]

        def t(root):
            if not root:
                return 0
            
            left=t(root.left)
            right=t(root.right)
            diff=abs(left-right)
            if diff>1:
                s[0]=False
                return 0

            return 1+max(left,right)
        t(root)

        return s[0]
        