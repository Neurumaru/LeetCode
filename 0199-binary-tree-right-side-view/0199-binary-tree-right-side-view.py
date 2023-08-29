# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cache = [0 for _ in range(100)]
        self.max_step = -1

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def recu(root: Optional[TreeNode], step: int):
            if not root:
                return
            recu(root.left, step + 1)
            self.cache[step] = root.val
            self.max_step = max(self.max_step, step)
            recu(root.right, step + 1)
        recu(root, 0)
        return self.cache[:self.max_step+1]