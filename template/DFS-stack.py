def dfs(graph, root):
    stack = []
    result = []

    stack.append(root)

    visited = set()
    visited.add(root)

    while len(stack) > 0:
        currentVertex = stack.pop()
        result.append(currentVertex)

        for neighbor in graph[currentVertex]:
            if neighbor in visited:
                continue
            stack.append(neighbor)
            visited.add(neighbor)
    return result


graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C"],
    "C": ["B", "E"],
    "D": ["A", "E"],
    "E": ["A", "D", "F", "C"],
    "F": ["E"],
}


print(dfs(graph, "A"))
# ['A', 'E', 'C', 'F', 'D', 'B']
