# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def DFS(self, root, pathStr, results):
        
        #If the node does not have any children
        if not root.left and not root.right:

            #Append the value of the node
            results.append(pathStr + str(root.val))
            
            #Exit
            return
            
        #If left child exists
        if root.left:
            
            #Append the value of the node and leading arrow
            self.DFS(root.left, pathStr + str(root.val) + '->', results)
            
        #If the right child exists
        if root.right:
            
            #Append the value of the node and leading arrow
            self.DFS(root.right, pathStr + str(root.val) + '->', results)
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        #If no root exists
        if not root:
            
            return []
        
        #Create a stack to keep track of the results
        results = []
        
        #DFS
        self.DFS(root, '', results)
        
        #Return the results
        return results