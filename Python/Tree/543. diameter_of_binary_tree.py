#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/diameter-of-binary-tree/
# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes
# in a tree. This path may or may not pass through the root.
#
"""
For example, given a binary tree:
                 1
               / \
             2    3
           / \
          4  5

Return 3, which is the length of the path [4, 2, 1, 3] or [5, 2, 1, 3].
"""
# Note: The length of path between two nodes is represented by the number of edges between them.
#
from Utils.timer_decorater import timer


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @timer
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def depth(node):
            if not node:
                return 0

            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1

        depth(root)

        return self.ans - 1

