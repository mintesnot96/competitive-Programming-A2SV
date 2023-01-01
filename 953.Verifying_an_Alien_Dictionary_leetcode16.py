class Solution:
    def isAlienSorted(self, W: List[str], O: str) -> bool:
        alpha_map = {c: i for i, c in enumerate(O)}
        for i in range(1, len(W)):
            prev_word = W[i - 1]
            curr_word = W[i]
            min_len = min(len(prev_word), len(curr_word))
            for j in range(min_len):
                prev_char = prev_word[j]
                curr_char = curr_word[j]
                if alpha_map[prev_char] < alpha_map[curr_char]:
                    break
                elif alpha_map[prev_char] > alpha_map[curr_char]:
                    return False
            else:
                if len(prev_word) > len(curr_word):
                    return False
        return True
# question
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
