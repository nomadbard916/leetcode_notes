#
# @lc app=leetcode id=815 lang=python3
# @lcpr version=30201
#
# [815] Bus Routes
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        # Key Insights

        # 1. Graph Representation: Think of this as a graph problem where:
        # - Nodes: Bus stops
        # - Edges: Buses that connect stops
        # - We want the shortest path measured in "number of buses" (not stops)

        # 2. Why BFS?:
        # BFS guarantees finding the shortest path in an unweighted graph.
        # Since each bus transfer has the same "cost" (1 bus), BFS is perfect.

        # 3. Two-Level Tracking:
        # - Track visited stops (to avoid revisiting stops unnecessarily)
        # - Track visited buses (to avoid taking the same bus twice)

        # Edge case: already at destination
        if source == target:
            return 0

        # build a graph: stop -> list of buses that pass through this stop
        # you may go bus-centric, but stop-centric is more frequent in our daily practices
        stop_to_buses: dict[int, List[int]] = defaultdict(list)
        for bus_id, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus_id)

        # BFS to find shortest path
        # queue stores: (current_stop, number_of_buses_taken)
        queue: deque[tuple[int, int]] = deque([(source, 0)])
        # to stop cyclic visits
        visited_stops: set[int] = {source}
        visited_buses: set[int] = set()

        while queue:
            current_stop, buses_taken = queue.popleft()

            # check if all buses pass through current stop
            for bus_id in stop_to_buses[current_stop]:
                # skip if we've already taken this bus, add immediately if we haven't
                if bus_id in visited_buses:
                    continue

                visited_buses.add(bus_id)

                # explore all stops on this bus route
                for next_stop in routes[bus_id]:
                    # found the target!
                    if next_stop == target:
                        return buses_taken + 1

                    # add unvisited stops to queue
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))

        return -1

        # Time & Space Complexity
        # Time Complexity: O(N × S)
        # - N = total number of stops across all routes
        # - S = number of distinct stops
        # - We visit each stop at most once, and for each stop, we check all buses serving it
        # - In worst case, we process all stops and all bus routes

        # Space Complexity: O(N + S)
        # - stop_to_buses: O(N) - stores all stop-bus relationships
        # - visited_stops: O(S) - at most S distinct stops
        # - visited_buses: O(B) where B is number of buses
        # - queue: O(S) in worst case


# @lc code=end


#
# @lcpr case=start
# [[1,2,7],[3,6,7]]\n1\n6\n
# @lcpr case=end

# @lcpr case=start
# [[7,12],[4,5,15],[6],[15,19],[9,12,13]]\n15\n12\n
# @lcpr case=end

#
