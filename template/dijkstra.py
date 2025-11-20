heap = [(0, start)]  # (cost, node)
min_cost = [inf] * n

while heap:
    cost, node = heapq.heappop(heap)  # ← Cost priority!

    if node == target:
        return cost  # ← Early termination

    for neighbor, price in graph[node]:
        new_cost = cost + price
        if new_cost < min_cost[neighbor]:
            min_cost[neighbor] = new_cost
            heapq.heappush(heap, (new_cost, neighbor))
