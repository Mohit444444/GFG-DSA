class Solution:
    def missingNumber(self, arr):
         n = len(arr) + 1  # Since one number is missing
         total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
         arr_sum = sum(arr)  # Sum of given elements
         return total_sum - arr_sum
        