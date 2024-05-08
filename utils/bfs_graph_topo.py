import collections

class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        G = collections.defaultdict(list)

        indegrees = {i: 0 for i in range(N)}
        for v, u in prerequisites:
            G[u].append(v)
            indegrees[v] += 1

        topo_order = []
        queue = collections.deque([u for u in range(N) if indegrees[u] == 0])
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v in G[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)

        if len(topo_order) != N:
            return []
            
        return topo_order
