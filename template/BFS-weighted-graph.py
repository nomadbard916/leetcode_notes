queue = deque([(start, 0)])  # (node, cost)
min_cost = [inf] * n
stops = 0

while queue and stops <= k:  # ← Level limiting!
    size = len(queue)
    for _ in range(size):  # ← Process entire level
        node, cost = queue.popleft()
        for neighbor, price in graph[node]:
            new_cost = cost + price
            if new_cost < min_cost[neighbor]:  # ← Cost tracking!
                min_cost[neighbor] = new_cost
                queue.append((neighbor, new_cost))
    stops += 1
