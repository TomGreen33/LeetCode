class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lo_idx = 0
        hi_idx = 0

        max_len = 0

        while hi_idx <= len(s):
            
            substring = s[lo_idx:hi_idx]
            
            if hi_idx < len(s):
                if s[hi_idx] in substring:
                    lo_idx += 1
                    
                else:
                    hi_idx += 1
            else:
                hi_idx += 1
                
            if len(substring) > max_len:
                max_len = len(substring)

        return max_len