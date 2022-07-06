"""
Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
def maxProduct(nums):
    """
    Solution Strategy:
    We need to keep track of both max and min (need to factor in negative numbers and 0).

    For ex. [2,3,-2,4]

    - > 3
    current element: 3
    Previous Max: 2
    Previous Min: 2

    The current min would be 2
    The current max would be 3

    Then current min would be previous min
    Then current max would be previous max

    But before that we need to check if the current max is greater than the result,
    because we are looking for the maximum product subarray.

    Essentially loop through all elements starting from index 1, since we will have index 0
    already stored in current(min/max), previous(min/max), and result.

    """
    current_min = nums[0]
    current_max = nums[0]
    previous_min = nums[0]
    previous_max = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        current_max = max(previous_max * nums[i], previous_min * nums[i], nums[i])
        current_min = min(previous_max * nums[i], previous_min * nums[i], nums[i])

        result = max(current_max, result)

        previous_max = current_max
        previous_min = current_min

    return print(result)


maxProduct([2,3,-2,4])
