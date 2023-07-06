class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # adjList = [[] for _ in range(n)]
        # for edge in edges:
        #     u, v = edge
        #     adjList[u].append(v)
        #     adjList[v].append(u)
        # visited = [False] * n

        # def dfs(curr):
        #     visited[curr] = True
        #     if curr == destination:
        #         return True
        #     for neighbor in adjList[curr]:
        #         if not visited[neighbor]:
        #             if dfs(neighbor):
        #                 return True
        #     return False

        # return dfs(source)
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parentx = find(x)
            parenty = find(y)
            if parentx != parenty:
                parent[parentx] = parenty
        for u, v in edges:
            union(u, v)
        return find(source) == find(destination)
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
