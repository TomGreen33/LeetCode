class Solution:
    def longestPalindrome(self, s: str) -> str:
        lo_idx = 0
        hi_idx = 1

        max_len = 0

        while hi_idx <= len(s):
            substring = s[lo_idx:hi_idx]

            if substring[-1::-1] == substring:
                if len(substring) > max_len:
                    max_substring = substring
                    max_len = len(substring)
                if lo_idx:
                    lo_idx -= 1
                    hi_idx += 1
                else:
                    hi_idx += 1
            else:
                delta = hi_idx - lo_idx

                if len(substring) > 3:
            
                    if delta % 2 == 0: # Even length
                        reset = (delta - 2) // 2
                    else: # Odd length
                        reset = (delta - 3) // 2
                    lo_idx += reset
                    hi_idx -= reset
                    

                if delta % 2 == 0: # Even length
                    hi_idx += 1
                else:
                    lo_idx += 1
        return max_substring