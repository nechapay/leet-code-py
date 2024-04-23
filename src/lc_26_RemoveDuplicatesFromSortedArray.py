# Given an integer array nums sorted in non-decreasing order, remove the duplicates in -place such
# that each unique element appears only once. The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in
# the order they were present in nums initially. The remaining elements of nums are not important as
# well as the size of nums.
# Return k.

def removeDuplicates(nums):
    # if not nums:
    #     return 0
    # s = set()
    # mx = max(nums) + 1
    # k = 0
    # for i in range(len(nums)):
    #     if nums[i] not in s:
    #         s.add(nums[i])
    #         k += 1
    #     else:
    #         nums[i] = mx
    # nums.sort()
    # return k
    k = 0
    last = None

    for n in nums:
        if last == n:
            continue
        last = n

        nums[k] = n
        k += 1

    return k


if __name__ == '__main__':
    print(removeDuplicates([1, 1, 2, 2, 2, 3, 3, 4]))
