class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        N = len(nums)
        out = set()

        for fourth in range(N):
            
            sub_nums = nums[:fourth] + nums[fourth+1:]    
            
            delta = (nums[fourth] - target) / 3
            
            sub_nums = [x + delta for x in sub_nums]
            
            p, n, z = [], [], []
            
            for num in sub_nums:
                if num>0:
                    p.append(num)
                elif num<0:
                    n.append(num)
                else:
                    z.append(num)
            
            N,P = set(n), set(p)
            
            P = {round(x,2) for x in P}
            N = {round(x,2) for x in N}
            
            # Case where 3 zeros exist
            if len(z) >= 3:
                out.add(tuple(sorted([nums[fourth], -delta, -delta, -delta])))
            
            # Case where a zero, and positive and negative with equal magnitude exist
            if z:
                for num in P:
                    if -num in N:
                        out.add(tuple(sorted([nums[fourth], round(-num-delta),round(-delta), round(num-delta)])))
            
            # Case where two negatives and a positive equal zero
            for i in range(len(n)):
                for j in range(i+1, len(n)):
                    num3 = round(-(n[i] + n[j]), 2)
                    if num3 in P:
                        out.add(tuple(sorted([nums[fourth], round(n[i]-delta), round(n[j]-delta), round(num3-delta)])))
                        
            # Case where two positives and a negative equal zero
            for i in range(len(p)):
                for j in range(i+1, len(p)):
                    num3 = round(-(p[i]+ p[j]), 2)
                    if num3 in N:
                        out.add(tuple(sorted([nums[fourth], round(p[i]-delta), round(p[j]-delta), round(num3-delta)])))



        out = [list(x) for x in out]

        return out