class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 1

        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return
        else:
            i -= 1

        j = len(nums) - 1

        while j >= i and nums[j] <= nums[i]:
            j -= 1
            
        nums[i], nums[j] = nums[j], nums[i]

        # This works because everything on the right is already sorted
        nums[i+1:] = reversed(nums[i+1:]) 
    


