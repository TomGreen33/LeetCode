class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1,5,10,50,100,500,1000]

        symbols = {1: "I",
                5: "V",
                10: "X",
                50: "L",
                100: "C",
                500: "D",
                1000: "M"}

        symbol = []

        while num:
            num_str = str(num)
            char = int(num_str[0])
            
            if char not in [4,9]:
                possible_values = [val for val in values if num - val >= 0]
                value = max(possible_values)
                symbol.append(symbols[value])
                num -= value
            
            # Subtractive Form
            elif char == 4:
                if len(num_str) == 3:
                    symbol.append("CD")
                    num -= 400
                elif len(num_str) == 2:
                    symbol.append("XL")
                    num -= 40
                elif len(num_str) == 1:
                    symbol.append("IV")
                    num -= 4
            
            elif char == 9:
                if len(num_str) == 3:
                    symbol.append("CM")
                    num -= 900
                elif len(num_str) == 2:
                    symbol.append("XC")
                    num -= 90
                elif len(num_str) == 1:
                    symbol.append("IX")
                    num -= 9

        symbol = "".join(symbol)
        return symbol