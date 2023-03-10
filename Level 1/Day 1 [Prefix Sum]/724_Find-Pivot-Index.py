"""
PROBLEM:
    Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
    Return the leftmost pivot index. If no such index exists, return -1.

EXAMPLE 1:
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11

EXAMPLE 2:
    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.

EXAMPLE 3:
    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0
 
CONSTRAINTS:
    1 <= nums.length <= 104
    -1000 <= nums[i] <= 1000
"""


from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(0, len(nums)):
            right_sum = right_sum - nums[i]

            if left_sum == right_sum:
                return i
            
            left_sum = left_sum + nums[i]
        
        return -1


if __name__ == "__main__":
    solution = Solution()

    # CASE 1
    result1 = solution.pivotIndex(nums = [1, 7, 3, 6, 5, 6])
    print(f"CASE 1 Result: {result1}")

    # Printing blank line seperator
    print()

    # CASE 2
    result2 = solution.pivotIndex(nums = [1, 2, 3])
    print(f"CASE 2 Result: {result2}")

    # Printing blank line seperator
    print()

    # CASE 3
    result3 = solution.pivotIndex(nums = [2, 1, -1])
    print(f"CASE 3 Result: {result3}")