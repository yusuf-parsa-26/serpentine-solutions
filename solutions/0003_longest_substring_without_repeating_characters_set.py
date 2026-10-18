class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        Set = set()
        length = 0

        while right < len(s):

            while s[right] in Set:
                Set.remove(s[left])
                left += 1
            length = max(length,right-left+1)
            Set.add(s[right])

            right += 1
        return length
