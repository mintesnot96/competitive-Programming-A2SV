https://leetcode.com/problems/satisfiability-of-equality-equations/

from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for equation in equations:
            x, operator, _, y = equation
            if operator == "=":
                union(x, y)

        for equation in equations:
            x, operator, _, y = equation
            if operator == "!":
                if find(x) == find(y):
                    return False

        return True
