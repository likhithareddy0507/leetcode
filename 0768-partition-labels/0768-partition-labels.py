class Solution:
    def partitionLabels(self, s):
        # Store the last index of each character in the string
        last_index = {char: idx for idx, char in enumerate(s)}
        
        # Initialize result list and pointers
        result = []
        start = 0
        end = 0

        # Traverse the string to determine partitions
        for idx, char in enumerate(s):
            # Update the furthest point to reach for this partition
            end = max(end, last_index[char])
            
            # If we reach the end of the current partition
            if idx == end:
                # Add partition size to the result
                result.append(end - start + 1)
                # Move start to the next partition
                start = idx + 1

        return result

# Example usage on LeetCode's platform
# Create an instance of the class
solution = Solution()

# Test cases
s1 = "ababcbacadefegdehijhklij"
s2 = "eccbbbbdec"

# Calling the method correctly with the instance
print("Output 1:", solution.partitionLabels(s1))  # Output: [9, 7, 8]
print("Output 2:", solution.partitionLabels(s2))  # Output: [10]