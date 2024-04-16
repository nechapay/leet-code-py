# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in d:
            return [d[diff], i]
        else:
            d[nums[i]] = i
    return []
