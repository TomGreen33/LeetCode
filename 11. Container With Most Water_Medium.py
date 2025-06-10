class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        
        lp = 0
        rp = len(height)-1
        
        while lp != rp:
            max_area = max(max_area, (rp-lp)*min(height[lp], height[rp]))
            
            if height[rp] > height[lp]:
                lp += 1
            else:
                rp -= 1
                
        return max_area   