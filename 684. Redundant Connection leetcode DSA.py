https://leetcode.com/problems/redundant-connection/description/
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[px] = py
            else:
                return True
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
