# https://leetcode.com/problems/number-of-provinces/description/
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited.add(city)
            for neighbor, connection in enumerate(isConnected[city]):
                if connection and neighbor not in visited:
                    dfs(neighbor)

        n = len(isConnected)
        visited = set()
        provinces = 0

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces
