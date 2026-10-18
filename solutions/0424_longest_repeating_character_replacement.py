class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        max_freq = 0
        max_len = 0 
        left = right = 0

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1

            max_freq = max(max_freq, freq[s[right]])

            r = (right - left + 1) - max_freq

            if r > k:
                freq[s[left]] -= 1
                left += 1

            max_len = right - left + 1  
            right += 1

        return max_len  
