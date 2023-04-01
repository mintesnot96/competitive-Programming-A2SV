class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans = ''
        for word in d:
            if len(word) < len(ans) or (len(word) == len(ans) and word > ans):
                continue
            i = 0
            for c in s:
                if i < len(word) and c == word[i]:
                    i += 1
            if i == len(word):
                ans = word
        return ans
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
