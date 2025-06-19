class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)
        N = len(nums)

        out = nums[0] + nums[1] + nums[2]

        best_delta = abs(out - target)

        for i in range(len(nums)):
            left = i+1
            right = N-1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                delta = abs(total - target)
                
                if delta == 0:
                    return target
                
                if delta < best_delta:
                    out = total
                    best_delta = delta
                
                # Need a bigger number
                if total < target:
                    left += 1
                
                # Need a smaller number 
                else:
                    right -= 1


        return out