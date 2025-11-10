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
        # Edge case: already at destination
        if source == target:
            return 0

        # build a graph: stop -> list of buses that pass through this stop
        stop_to_buses: dict[int, List[int]] = defaultdict(list)
        for bus_id, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus_id)

        # BFS to find shortest path
        # queue stores: (current_stop, number_of_buses_taken)
        queue: deque[tuple[int, int]] = deque([(source, 0)])
        visited_stops: set[int] = {source}
        visited_buses: set[int] = set()

        while queue:
            current_stop, buses_taken = queue.popleft()

            # check if all buses that pass through current stop
            for bus_id in stop_to_buses[current_stop]:
                # skip if we've already taken this bus
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


# @lc code=end


#
# @lcpr case=start
# [[1,2,7],[3,6,7]]\n1\n6\n
# @lcpr case=end

# @lcpr case=start
# [[7,12],[4,5,15],[6],[15,19],[9,12,13]]\n15\n12\n
# @lcpr case=end

#
