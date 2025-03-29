class Solution:
	def minJumps(self, arr):
	    # code here
        n = len(arr)
        if n == 1:
            return 0  # Already at the last index
            
        if arr[0] == 0:
            return -1  # Cannot move forward

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):  # Don't need to jump from the last element
            farthest = max(farthest, i + arr[i])  # Update farthest reachable index

            if i == current_end:  # Time to jump
                jumps += 1
                current_end = farthest  # Move current_end to farthest reachable index

                if current_end >= n - 1:  # If we can reach or pass the last index
                    return jumps

        return -1  # If we finish the loop and haven't reached the last index