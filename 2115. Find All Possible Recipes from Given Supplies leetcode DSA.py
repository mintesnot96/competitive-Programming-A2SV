import collections
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        available_supplies = set(supplies)
        graph = collections.defaultdict(list)
        inDegree = collections.Counter()
        q = collections.deque()

        # Build graph
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in available_supplies:
                    graph[ingredient].append(recipe)
                    inDegree[recipe] += 1

        # Topology
        for recipe in recipes:
            if inDegree[recipe] == 0:
                q.append(recipe)

        while q:
            u = q.popleft()
            ans.append(u)
            for v in graph[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)

        return ans
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
