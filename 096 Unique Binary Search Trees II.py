"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        dfs
        Catalan: https://www.youtube.com/watch?v=QdcujZTp_8M (Forth proof)
        :param n: integer
        :return: list of TreeNode
        """
        if n==0:
            return [None]

        return self.generate(1, n)

    def generate(self, start, end):
        """
        dfs without dp
        {number| number \in [start, end]}

        Follow the 1st proof of Catalan Number
        :param start: initial number in the array
        :param end: final number in the array
        :return: list of TreeNode
        """
        subtree_roots = []

        # trivial
        if start>end:
            subtree_roots.append(None)
            return subtree_roots

        # pivot
        # list of unique subtrees = list of unique left subtrees, pivot, list of unique right subtrees
        for pivot in range(start, end+1):
            left_subtree_roots = self.generate(start, pivot-1)  # no dp yet
            right_subtree_roots = self.generate(pivot+1, end)  # no dp yet

            for left_node in left_subtree_roots:
                for right_node in right_subtree_roots:
                    pivot_node = TreeNode(pivot)
                    pivot_node.left = left_node
                    pivot_node.right = right_node

                    subtree_roots.append(pivot_node)


        return subtree_roots

