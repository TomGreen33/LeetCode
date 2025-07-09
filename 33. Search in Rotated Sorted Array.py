class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)

        if N == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        left = 0
        right = N - 1

        while left < right:
            mid = (left + right) // 2
            
            # If we found the target
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right 
            
            if left == right - 1:
                return -1

            # If the decrease is on the right side
            if nums[mid] > nums[left]:
                # If it is the continuous range between left and mid (which has no decrease)
                if (target >= nums[left]) and (target <= nums[mid]):
                    right = mid
                else:
                    left = mid
            
            # If the decrease is on the left side
            else:
                if (target >= nums[mid]) and (target <= nums[right]):
                    left = mid
                else:
                    right = mid