# 从 s 开始 BFS 遍历图的所有节点，且记录遍历的步数
from collections import deque


def bfs(graph, s):
    visited = [False] * len(graph)
    q = deque([s])
    visited[s] = True
    # 记录从 s 开始走到当前节点的步数
    step = 0

    while q:
        q_len = len(q)
        for i in range(q_len):
            cur = q.popleft()
            print(f"visit {cur} at step {step}")
            # 判断是否到达终点
            if cur == target:
                return step

            # 将邻居节点加入队列，向四周扩散搜索
            for to in neighborsOf(cur):
                if not visited[to]:
                    q.append(to)
                    visited[to] = True
        step += 1
    # 如果走到这里，说明在图中没有找到目标节点
    return -1
