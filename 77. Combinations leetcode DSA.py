class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(combination, index):
            if len(combination) == k:
                result.append(combination[:])
                # return
            for i in range(index, n+1):
                combination.append(i)
                backtrack(combination, i+1)
                combination.pop()
        
        result = []
        backtrack([], 1)
        return result
# https://leetcode.com/problems/combinations/description/
