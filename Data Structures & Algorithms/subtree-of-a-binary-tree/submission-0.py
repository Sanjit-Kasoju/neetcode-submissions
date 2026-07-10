# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        def compare(root,subroot):
            if not root and not subroot:
                return True

            if (not root and subroot) or (not subroot and root):
                return False

            if root.val!=subroot.val:
                return False
            return compare(root.left,subroot.left) and compare(root.right,subroot.right)

        def mtree(root):
            if not root:
                return False
            
            if compare(root,subroot):
                return True

            return mtree(root.left) or mtree(root.right)
        return mtree(root)

        