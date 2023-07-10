# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(len(s1)):
            char1, char2 = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            parent1, parent2 = find(char1), find(char2)
            if parent1 < parent2:
                parent[parent2] = parent1
            else:
                parent[parent1] = parent2

        result = []
        for char in baseStr:
            char = ord(char) - ord('a')
            result.append(chr(find(char) + ord('a')))
        return ''.join(result)
