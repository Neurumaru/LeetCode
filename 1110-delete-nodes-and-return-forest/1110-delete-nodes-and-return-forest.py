# ayaan.jun
from typing import Optional, List, Set, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete: Set[TreeNode] = set(to_delete)
        res: List[TreeNode] = []
        q: Set[Tuple[TreeNode, bool]] = {tuple([root, True])}
        while q:
            n, r = q.pop()
            if n == None:
                continue
            if r and n.val not in to_delete:
                res.append(n)
            q.add(tuple([n.right, n.val in to_delete]))
            q.add(tuple([n.left, n.val in to_delete]))
            if n.left != None and n.left.val in to_delete:
                n.left = None
            if n.right != None and n.right.val in to_delete:
                n.right = None
        return res
