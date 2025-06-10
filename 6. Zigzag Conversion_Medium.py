import numpy as np

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        remainder = len(s)

        cols = []
        idx = 0
        divisor = numRows-1


        if divisor:
            while remainder > 0:
                if idx % divisor == 0:
                    cols.append(-min(numRows, remainder))
                    remainder -= min(numRows, remainder)
                else:
                    cols.append(idx % divisor)
                    remainder -= 1
                
                idx = idx + 1
            
            print(cols)
            
            string = []
            matrix = np.zeros((numRows, len(cols)), dtype = "object")
            
            for j, col in enumerate(cols):
                if col < 0:
                    matrix[:-col,j] = [x for x in s[:-col]]
                    s = s[-col:]
                else:
                    matrix[-col-1,j] = s[0]
                    s = s[1:]
            
            string = []
            for row in matrix:
                for char in row:
                    if char:
                        string.append(char)
            string = "".join(string)
            return string 
            
        else:
            return s





