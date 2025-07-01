# Pattern: Modify tree while traversing with post order
def modify_tree(node):
    if not node:
        return None

    # there can be pre order logic, but not for tree modification

    # Process children first (post-order style)
    node.left = modify_tree(node.left)
    node.right = modify_tree(node.right)

    # * post order logic
    # Then decide what to do with current node
    if should_modify(node):
        return transform(node)
    return node
