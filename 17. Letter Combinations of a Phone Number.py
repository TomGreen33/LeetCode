class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
                
        lookup = {"2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]}

        combinations = [""]

        for char in digits:
            letters = lookup[char]
            
            new_combinations = []
            
            for combination in combinations:
                for letter in letters:
                    new_combination = combination + letter
                    new_combinations.append(new_combination)
                    
            combinations = new_combinations 

        try:
            combinations.remove("")
        except:
            pass

        return combinations