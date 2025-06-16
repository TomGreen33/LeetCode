class Solution:
    def myAtoi(self, s: str) -> int:

        if s:

            for i, char in enumerate(s):
                if char != " ":
                    break

            s = s[i:]

            if s[0] == "-":
                is_neg = True
                limit = 2 ** 31
                s = s[1:]
            elif s[0] == "+":
                is_neg = False
                s = s[1:]
                limit = 2 ** 31 - 1
            else:
                is_neg = False
                limit = 2 ** 31 - 1

            for i, char in enumerate(s):
                if char != "0":
                    break

            s = s[i:]

            truncate = False
            for i, char in enumerate(s):
                if char.isdigit() == False:
                    truncate = True
                    break
            if not truncate:
                i += 1
                
            s = s[:i]
            if s:
                out = int(s)
                
                if abs(out) > limit:
                    out = limit
                
                if is_neg:
                    out = -out
            else:
                out = 0
            
        else:
            out = 0
        
        return out