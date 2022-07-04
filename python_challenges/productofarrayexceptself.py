"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""
def productExceptSelf(nums):
    left_product = []

    #Creating the prefix (multiplying from the left side)
    #[1,2,6,24]
    for i in range(0, len(nums)):
        if i == 0: #If first number
            left_product.append(nums[i])
        else:
            left_product.append(left_product[i-1] * nums[i])

    print(left_product)
    right_product = []

    #Creating the postfix (multiplying from the right side)
    #[24,24,12,4]
    j = 0
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1: #If last number, append to list
            right_product.append(nums[i])
        else:
            right_product.append(right_product[j-1] * nums[i])
        j += 1
        right_product_new = right_product[::-1]

    print(right_product_new)
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(1 * right_product_new[i + 1])
        elif i == len(nums) - 1:
            result.append(left_product[i - 1] * 1)
        else:
            result.append(left_product[i - 1] * right_product_new[i + 1])

    return print(result)

def productExceptSelfSimplified(nums):
    prefix = 0
    postfix = 0

    #Creating an array that is the size of nums
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1

    for i in range(len(nums), -1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result

productExceptSelf([1,2,3,4])
#productExceptSelfSimplified([1,2,3,4])


