class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0] #flower ["flower","flow","flight"]
        count=0
        isFound = True
        for i in range(len(first)):
            for word in strs:
                if i> len(word)-1:
                    isFound = False
                    break
                if first[i] == word[i]:
                    isFound=True
                else:
                    isFound = False
                    break
            if isFound:
                count+=1
            else:
                break
        return first[:count]
#  Question link
# https://leetcode.com/problems/longest-common-prefix/submissions/869235447/
