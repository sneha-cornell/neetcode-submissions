# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')
        def gain(node):
            if not node: 
                return 0
            #calculate max downward gain from each side, clamp negatives to 0
            left=max(gain(node.left),0)
            right=max(gain(node.right),0)
            #global max- bends and takes both side paths
            self.best = max(self.best,node.val+left+right)
            #return only a straight path that parent can extend 
            return node.val+max(left,right)
        gain(root)
        return self.best 