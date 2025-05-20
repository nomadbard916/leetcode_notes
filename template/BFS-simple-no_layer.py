import collections

def bfs(root):
    if root is None:
        return
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if (node ): # is the node we're looking for
            return node
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return -1
