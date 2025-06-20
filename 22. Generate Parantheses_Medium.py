class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        out = []

        def build_permutations(left, right, string):
            
            # This permutation is done
            if len(string) == 2 * n:
                out.append(string)
            
            else:
                # Can still add opening parantheses
                if left < n:
                    build_permutations(left+1, right, string + "(")
                
                # Can add closing parantheses
                if left > right:
                    build_permutations(left, right+1, string + ")")
                    
                    
        build_permutations(0,0,"")

        return out