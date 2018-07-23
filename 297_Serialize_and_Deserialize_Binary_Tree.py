"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        result = []
        queue = [root]
        while len(queue) > 0:
            x = queue.pop(0)
            if x:
                result.append(str(x.val))
                queue.append(x.left)
                queue.append(x.right)        
            else:
                result.append('null')
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        x = data.split(",")
        root = TreeNode(None)
        root.val = x.pop(0)
        queue = [root]
        while len(x) > 0 and len(queue) > 0:
            current_node = queue.pop(0)

            left = right = None
            left_val = x.pop(0)
            if left_val != 'null':
                left = TreeNode(left_val)
                queue.append(left)

            right_val = x.pop(0)
            if right_val != 'null':
                right = TreeNode(right_val)
                queue.append(right)
            current_node.left = left
            current_node.right = right
        return root
