def dfs(graph, root):
    stack = []
    result = []

    stack.append(root)

    # actually we can just check against 'result'.
    # making another 'visited' container just makes the concept clearer.
    # see below for another implementation.
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


# sol2
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()

        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)

    return discovered


# adjacency list graph
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

print(iterative_dfs(1))
