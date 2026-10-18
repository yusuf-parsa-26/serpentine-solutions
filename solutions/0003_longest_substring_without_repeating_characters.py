class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0

        prev_idx = {}
        length = 0
        
        while right < len(s):

            if s[right] in prev_idx and prev_idx[s[right]] >= left:
                left = prev_idx[s[right]] + 1
            
            length = max(length,right-left+1)

            prev_idx[s[right]] = right
            right += 1

        return length
