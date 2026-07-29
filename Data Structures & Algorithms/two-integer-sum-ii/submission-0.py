from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at opposite ends of the sorted array
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-indexed results as required by the problem statement
                return [left + 1, right + 1]
            elif current_sum < target:
                # Sum is too small, increase the smaller value by moving right
                left += 1
            else:
                # Sum is too large, decrease the larger value by moving left
                right -= 1
                
        return []
