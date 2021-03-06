"""
Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

"""
def maxSubArray(nums):

    #Creating a dp list that is the size of nums
    dp = [0 for i in range(len(nums))]

    #First element in the list is the same as nums
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        #Getting the max between the last subarray or the current element
        dp[i] = max(dp[i - 1] + nums[i],nums[i])

    return max(dp)

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
