class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        p, n, z = [], [], []

        for num in nums:
            if num>0:
                p.append(num)
            elif num<0:
                n.append(num)
            else:
                z.append(num)

        N,P = set(n), set(p)

        # Case where 3 zeros exist
        if len(z) >= 3:
            out.add((0,0,0))

        # Case where a zero, and positive and negative with equal magnitude exist
        if z:
            for num in P:
                if -num in N:
                    out.add((-num, 0, num))

        # Case where two negatives and a positive equal zero
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                num3 = -(n[i] + n[j])
                if num3 in P:
                    out.add(tuple(sorted([n[i], n[j], num3])))
                    
        # Case where two positives and a negative equal zero
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                num3 = -(p[i]+ p[j])
                if num3 in N:
                    out.add(tuple(sorted([p[i], p[j], num3])))
        out = [list(x) for x in out]
        return out