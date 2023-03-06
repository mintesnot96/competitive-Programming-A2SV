

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if not word1 or not word2:
            return word1 + word2
        
        if word1 > word2:
            return word1[0] + largest_merge(word1[1:], word2)
        elif word2 > word1:
            return word2[0] + largest_merge(word1, word2[1:])
        else:
            # tiebreak by comparing suffixes
            if word1[1:] > word2[1:]:
                return word1[0] + largest_merge(word1[1:], word2)
            else:
                return word2[0] + largest_merge(word1, word2[1:])
# https://leetcode.com/problems/largest-merge-of-two-strings/
