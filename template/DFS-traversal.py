# 二叉树的遍历框架
def traverse(root):
    if root is None:
        return
    # 前序位置
    traverse(root.left)
    # 中序位置
    traverse(root.right)
    # 后序位置
