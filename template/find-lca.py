from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_lca(node: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
    if not node:
        return None

    if node.val == p or node.val == q:
        return node

    left = find_lca(node.left, p, q)
    right = find_lca(node.right, p, q)

    # This means both p and q were found in different subtrees, so root is their LCA.
    if left and right:
        return node

    # If one is not None, propagate that node up the recursion.
    return left or right
