class Solution:
    def sortArray(self, nums):
        return self.merge_sort(nums)
    
    def merge_sort(self, nums):
        if len(nums) > 1:
            # Find the middle of the array
            mid = len(nums) // 2
            
            # Divide the array elements into two halves
            left_half = nums[:mid]
            right_half = nums[mid:]
            
            # Recursively sort both halves
            self.merge_sort(left_half)
            self.merge_sort(right_half)
            
            # Merge the sorted halves
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1
            
            # Check for any remaining elements
            while i < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1
        return nums

# Example Usage
# The following lines are for testing locally; LeetCode will handle the input/output.
nums1 = [5, 2, 3, 1]
nums2 = [5, 1, 1, 2, 0, 0]

solution = Solution()
print(solution.sortArray(nums1))  # Output: [1, 2, 3, 5]
print(solution.sortArray(nums2))  # Output: [0, 0, 1, 1, 2, 5]
        