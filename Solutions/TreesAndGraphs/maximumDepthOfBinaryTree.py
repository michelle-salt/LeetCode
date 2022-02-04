# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepthHelper(root: Optional[TreeNode]) -> int:
    if root == None:
        return 0
    return 1 + max(maxDepthHelper(root.left), maxDepthHelper(root.right))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(maxDepthHelper(root.left), maxDepthHelper(root.right))
        
