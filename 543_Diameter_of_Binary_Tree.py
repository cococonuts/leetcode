"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or (root.left == None and root.right == None):
            return 0
        self.max_path = 0
        def get_path(root):
            left = 0
            right = 0
            if root.left != None:
                left = get_path(root.left) + 1
            if root.right != None:
                right = get_path(root.right) + 1
            self.max_path = max(self.max_path, left+right)
            return max(right, left)
        get_path(root)
        return self.max_path
