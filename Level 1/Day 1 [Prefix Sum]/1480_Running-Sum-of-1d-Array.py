"""
PROBLEM:
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.


EXAMPLE 1:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

EXAMPLE 2:
    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

EXAMPLE 3:
    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]

CONSTRAINTS:
    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6
"""


from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        for i in range(len(nums) - 1, -1, -1):
            running_sum.append(sum(nums[:i+1]))

        return running_sum[::-1]


if __name__ == "__main__":
    solution = Solution()

    # CASE 1
    result1 = solution.runningSum(nums = [1, 2, 3, 4])
    print(f"CASE 1 Result: {result1}")

    # Printing blank line seperator
    print()

    # CASE 2
    result2 = solution.runningSum(nums = [1, 1, 1, 1, 1])
    print(f"CASE 2 Result: {result2}")

    # Printing blank line seperator
    print()

    # CASE 3
    result3 = solution.runningSum(nums = [3, 1, 2, 10, 1])
    print(f"CASE 3 Result: {result3}")