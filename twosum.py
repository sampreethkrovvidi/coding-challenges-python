"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

def twoSum(nums, target):

    #Time complexity O(n^2)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return print([i,j])

def twoSumOptimal(nums, target):    

    #Using Hashmap to get time complexity of O(n)
    hashmap = {}

    for i in range(len(nums)):
        hashmap[nums[i]] = i

    #2,7,11,15,...
    #0,1,2,3,...

    for i in range(len(nums)):
        if target - nums[i] in hashmap and hashmap[target-nums[i]] != i:
            return print([hashmap[target-nums[i]], i])

twoSum([2,7,11,15], 9)
#twoSumOptimal([2,7,11,15], 9)


