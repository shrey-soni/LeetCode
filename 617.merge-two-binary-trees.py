#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def add(r1,r2):
            if not r1 :
                return r2
            elif not r2:
                return r1
            else:
                r1.left=add(r1.left,r2.left)
                r1.right=add(r1.right,r2.right)
                r1.val=r1.val+r2.val
                return r1
        return add(root1,root2)
# @lc code=end