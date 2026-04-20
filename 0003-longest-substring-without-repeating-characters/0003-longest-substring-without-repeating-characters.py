class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        freq = {}
        max_len = 0

        left = 0
        right = 0

        while right < len(s):

            if s[right] in freq:
                left = max(freq[s[right]] + 1, left)
            
            freq[s[right]] = right

            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len

