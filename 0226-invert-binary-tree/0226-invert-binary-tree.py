# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #Base 1: There is no tree
        if not root:
            
            return None
        
        #Base case 2: It is a node with no children
        if root.left is None and root.right is None:
            
            return root
        
        else:
            
            temp = root.left
            root.left = root.right
            root.right = temp
            
            if root.left is not None:
                
                self.invertTree(root.left)
                
            if root.right is not None:
                
                self.invertTree(root.right)
                
            return root