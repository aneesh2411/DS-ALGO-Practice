"""
Problem: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers in the array
such that they add up to target. You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    # Create a hash map to store complements
    num_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in map, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
            
        # Add current number and its index to the map
        num_map[num] = i
    
    return []  # No solution found

def test_two_sum():
    # Test case 1: Basic case
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case 2: Numbers in different order
    assert two_sum([3, 2, 4], 6) == [1, 2]
    
    # Test case 3: Same numbers
    assert two_sum([3, 3], 6) == [0, 1]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_two_sum() 