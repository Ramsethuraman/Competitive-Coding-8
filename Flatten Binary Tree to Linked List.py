# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
Flatten Binary Tree to Linked List
Time - O(N)
Space - O(1)
"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                return root
            l=dfs(root.left)
            r=dfs(root.right)
            if l:
                l.right=root.right
                root.right=root.left
                root.left=None
            return r if r else l
        return dfs(root)