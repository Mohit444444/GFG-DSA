class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        max_sum = float('-inf')  # Initialize max_sum to the smallest possible value
        current_sum = 0  # Current subarray sum

        for num in arr:
            current_sum += num  # Add current element to current_sum
            max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is greater
            if current_sum < 0:  
                current_sum = 0  # Reset if current sum is negative

        return max_sum  # Return the maximum sum found


    #   Time Complexity: O(n)
    #   Space Complexity: O(1)