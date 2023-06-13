# https://leetcode.com/problems/beautiful-arrangement/
class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(start, visited):
            if start > n:
                return 1

            res = 0
            for i in range(1, n + 1):
                if not visited[i] and (i % start == 0 or start % i == 0):
                    visited[i] = True
                    res += backtrack(start + 1, visited)
                    visited[i] = False

            return res

        visited = [False] * (n + 1)
        return backtrack(1, visited)
