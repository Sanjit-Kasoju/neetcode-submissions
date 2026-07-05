# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        s=[0]

        def t(root):
            if not root:
                return 0
            
            left=t(root.left)
            right=t(root.right)
            diameter=left+right

            s[0]=max(s[0],diameter)

            return 1+max(left,right)
        t(root)

        return s[0]
        