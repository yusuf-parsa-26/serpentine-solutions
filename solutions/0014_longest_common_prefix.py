class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s = ""
        if len(strs) == 0:
            return ""
        for j in range(len(strs[0])):
            for i in range(1,len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    return s
            s += strs[0][j]
        return s
