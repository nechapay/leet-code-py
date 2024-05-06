# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a
# given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

def searchRange(nums, target):
    left = 0
    right = len(nums) - 1
    lb = len(nums)

    while left <= right:
        mid = (left+right) // 2

        if nums[mid] >= target:
            lb = mid
            right = mid - 1
        else:
            left = mid + 1

    if lb >= len(nums) or nums[lb] != target:
        return [-1, -1]

    rb = len(nums)
    left = lb + 1
    right = len(nums) - 1

    while left <= right:
        mid = (left+right) // 2
        if nums[mid] > target:
            rb = mid
            right = mid - 1
        else:
            left = mid + 1

    return [lb, rb - 1]


if __name__ == '__main__':
    print(searchRange([0, 0, 0, 0, 0, 0, 0], 0))
