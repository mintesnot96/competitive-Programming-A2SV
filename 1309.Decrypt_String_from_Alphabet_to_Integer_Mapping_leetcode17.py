class Solution:
    def freqAlphabets(self, s: str) -> str:
        letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
        final_string = ''
        i = len(s) - 1
        while i >= 0:
            print(f" {i} ")
            if s[i] == "#":
                final_string = letter[int(s[i - 2:i])-1] + final_string
                i = i - 3
            else:
                final_string = letter[int(s[i]) - 1] + final_string
                i -= 1
        return final_string


# question link
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
