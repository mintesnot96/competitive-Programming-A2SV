class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord=''
        if len(word1)<len(word2):
            for i in range(len(word1)):
                newWord=newWord+word1[i]+word2[i]
                if i==len(word1)-1 and i<len(word2)-1:
                    return newWord+word2[i+1:]
        else:
            for i in range(len(word2)):
                newWord=newWord+word1[i]+word2[i]
                if i==len(word2)-1 and i<len(word1)-1:
                    return newWord+word1[i+1:]
        return newWord
# question link
# https://leetcode.com/problems/merge-strings-alternately/description/
