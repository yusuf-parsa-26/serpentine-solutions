class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len = len(s)
        p_len = len(p)
        result = []

        if p_len > s_len:
            return []
        left = right = 0
        freq = [0]*26
        temp_freq = [0]*26

        for c in p:
            freq[ord(c) - ord('a')] += 1
        
        while right < s_len:
            temp_freq[ord(s[right])-ord('a')] += 1

            if right-left+1 == p_len:
                if temp_freq == freq:
                    result.append(left)
                
                temp_freq[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            right += 1
        
        return result
