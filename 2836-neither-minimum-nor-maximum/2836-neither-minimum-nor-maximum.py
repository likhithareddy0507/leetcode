class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the length of nums is less than 3, return -1 since we cannot have a middle element
        if len(nums) < 3:
            return -1
        
        # Sort the array
        nums.sort()
        
        # Return the second element which will always be between the minimum and maximum
        return nums[1]
        