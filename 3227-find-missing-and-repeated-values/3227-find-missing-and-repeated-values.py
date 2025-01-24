class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid) * len(grid[0])  # Total numbers in the grid
        expected_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
        expected_square_sum = n * (n + 1) * (2 * n + 1) // 6  # Sum of squares of numbers from 1 to n
        
        actual_sum = 0
        actual_square_sum = 0
        seen = set()
        repeated_value = -1
        
        for row in grid:
            for num in row:
                actual_sum += num
                actual_square_sum += num * num
                if num in seen:
                    repeated_value = num
                seen.add(num)
        
        # Difference between expected and actual sums
        sum_diff = expected_sum - actual_sum
        square_sum_diff = expected_square_sum - actual_square_sum
        
        # Calculate the missing and repeated values
        missing_value = (sum_diff + square_sum_diff // sum_diff) // 2
        repeated_value = missing_value - sum_diff
        
        return [repeated_value, missing_value]
        