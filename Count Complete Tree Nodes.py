#Given a complete binary tree, count the number of nodes.
#
#Note:
#
#Definition of a complete binary tree from Wikipedia:
#In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
#Example:
#
#Input: 
#    1
#   / \
#  2   3
# / \  /
#4  5 6
#
#Output: 6


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_subtree = self.left_depth(root.left)
        right_subtree = self.left_depth(root.right)

        if left_subtree == right_subtree:
            return 2**left_subtree + self.countNodes(root.right)    # 1 (root) + 2**left_subtree - 1 (left subtree)
        else:
            return 2**right_subtree + self.countNodes(root.left)


    def left_depth(self, node):
        depth = 0
        while node:
            node = node.left
            depth += 1
        return depth
        
