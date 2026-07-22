# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #input treenode graph , 2 treenode references of nodes 
        #output treenode LCA of 2 nodes 
        #BST has ordering not like ordinary binary tree
        #node can be its own ancestor 

        # #base case 
        # if not root or root.val==p.val or root.val==q.val:
        #     return root
        # left= self.lowestCommonAncestor(root.left,p,q)
        # right=self.lowestCommonAncestor(root.right,p,q)
        # if left and right: 
        #     return root 
        # return left if left else right  
         while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


