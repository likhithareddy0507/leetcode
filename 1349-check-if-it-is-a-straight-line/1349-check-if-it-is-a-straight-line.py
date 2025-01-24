class Solution:
    def checkStraightLine(self, coordinates):
        # Ensure there are at least two points to compare
        if len(coordinates) < 2:
            return False

        # Extract the first two points
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        # Loop through the remaining points starting from the third point
        for i in range(2, len(coordinates)):
            x3, y3 = coordinates[i]

            # Cross multiplication check for collinearity
            if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
                return False
        return True

# Example usage for LeetCode (will work when submitted):
coordinates1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
coordinates2 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]

# Create an instance of the class
solution = Solution()
print(solution.checkStraightLine(coordinates1))  # Output: True
print(solution.checkStraightLine(coordinates2))  # Output: False


        