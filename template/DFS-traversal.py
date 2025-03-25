# 二叉树的遍历框架
# 基本的二叉树节点
class BTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def b_tree_traverse(root: BTreeNode | None):
    if root is None:
        return
    # 前序位置
    b_tree_traverse(root.left)
    # 中序位置
    b_tree_traverse(root.right)
    # 后序位置


# 基本的 N 叉树节点
class TreeNode:
    val: int
    children: List[TreeNode]  # type: ignore  # noqa: F821


def traverse(root: TreeNode) -> None:
    for child in root.children:
        traverse(child)
    # for graphs with potential circulations, use a bool array "visit" to take record
