# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #input treenode graph
        #output length of longest path
        #length measured in edges not nodes 
        #sub tree (no need to pass thru root) - considers every node as a pivot,
        #tracking of max 
        self.best=0
        def dfs(node):
            if not node: 
                return 0
            left = dfs(node.left)
            right=dfs(node.right)
            self.best = max(self.best, left+right)
            return 1+max(left,right)
        dfs(root)
        return self.best  

